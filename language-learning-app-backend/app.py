from flask import Flask, request, jsonify
from flask_cors import CORS
from firebase_admin import auth
from config import firebase_app
from firebase_admin import firestore
import json

app = Flask(__name__)
CORS(app)

db = firestore.client()

@app.route('/api/auth/verify-token', methods=['POST'])
def verify_token():
    try:
        # Get token from request
        token = request.json.get('token')
        if not token:
            return jsonify({'error': 'No token provided'}), 400

        # Verify token
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        return jsonify({
            'user_id': user_id,
            'email': decoded_token.get('email'),
            'name': decoded_token.get('name')
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 401

@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    try:
        # Get token from header
        token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        # Fetch user data from Firestore
        user_doc = db.collection('users').document(user_id).get()
        
        if not user_doc.exists:
            return jsonify({
                'error': 'User profile not found'
            }), 404
            
        user_data = user_doc.to_dict()
        return jsonify(user_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Get languages list endpoint
@app.route('/api/languages', methods=['GET'])
def get_languages():
    try:
        doc_ref = db.collection('languages').document('languageCodes')
        doc = doc_ref.get()
        if doc.exists:
            return jsonify(doc.to_dict())
        return jsonify({'error': 'Languages not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create user profile endpoint
@app.route('/api/user/create-profile', methods=['POST'])
def create_user_profile():
    try:
        token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        db.collection('users').document(user_id).set(
            {
                "userId": user_id,
                "lastLoggedInDate": firestore.SERVER_TIMESTAMP,
                "languages": request.json.get('languages', []),
                "email": decoded_token.get('email'),
                "name": decoded_token.get('name'),
                "streakDays": 0,
                "totalPoints": 0,
                "createdDate": firestore.SERVER_TIMESTAMP
            }
        )
        return jsonify({'message': 'Successful'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/onboarding/questions', methods=['GET'])
def get_onboarding_questions():
    try:
        db = firestore.client()
        questions_ref = db.collection('onboarding').document('questions')
        doc = questions_ref.get()
        
        if doc.exists:
            return jsonify(doc.to_dict())
        return jsonify({'error': 'Questions not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/onboarding/save', methods=['POST'])
def save_onboarding():
    try:
        # Get token from header
        token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        # Get selected answers from request body
        answers = request.json.get('answers')
        
        if not answers:
            return jsonify({'error': 'No answers provided'}), 400
            
        # Update user document in Firestore
        user_ref = db.collection('users').document(user_id)
        user_ref.update({
            'onboardingQuestions': answers
        })
        
        return jsonify({'message': 'Onboarding data saved successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
@app.route('/api/user/check-onboarding', methods=['GET'])
def check_onboarding():
    try:
        # Get token from header
        token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        # Get user document from Firestore
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        
        if not user_doc.exists:
            return jsonify({'hasCompletedOnboarding': False})
            
        user_data = user_doc.to_dict()
        has_completed = 'onboardingQuestions' in user_data
        
        return jsonify({'hasCompletedOnboarding': has_completed})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
@app.route('/api/user/add-language', methods=['POST'])
def add_language():
    try:
        token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        language_data = request.json
        
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        
        if not user_doc.exists:
            return jsonify({'error': 'User not found'}), 404
            
        user_data = user_doc.to_dict()
        languages = user_data.get('languages', [])
        languages.append(language_data)
        
        user_ref.update({'languages': languages})
        
        return jsonify(user_ref.get().to_dict())
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/api/lessons/<language>', methods=['GET'])
def get_lessons(language):
    try:
        # Get lessons from Firestore for the specified language
        lessons = db.collection('lessons').document(f'{language}').get().to_dict()
        return jsonify(lessons), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/user/complete-lesson', methods=['POST'])
def complete_lesson():
    try:
        token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        
        lesson_data = request.json
        lesson_type = lesson_data.get('type')
        lesson_id = lesson_data.get('id')
        
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        
        if not user_doc.exists:
            return jsonify({'error': 'User not found'}), 404
            
        user_data = user_doc.to_dict()
        completed_lessons = user_data.get('completedLessons', [])
        
        # Add lesson to completed list if not already present
        lesson_key = f"{lesson_type}_{lesson_id}"
        if lesson_key not in completed_lessons:
            completed_lessons.append(lesson_key)
            
        # Calculate progress
        total_lessons = 15  # Assuming 5 lessons each for grammar, audio, vocabulary
        progress = (len(completed_lessons) / total_lessons) * 100
        
        # Update user document
        user_ref.update({
            'completedLessons': completed_lessons,
            'progress': progress
        })
        
        return jsonify({'progress': progress}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)