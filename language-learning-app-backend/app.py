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
        
        # Here you would typically fetch user data from your database
        # For now, returning basic info from token
        return jsonify({
            'uid': decoded_token['uid'],
            'email': decoded_token.get('email'),
            'name': decoded_token.get('name'),
            'selected_language': 'English',  # Default value
            'progress': {
                'completed_lessons': 0,
                'total_points': 0
            }
        })
        
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
                "name": decoded_token.get('name')
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

if __name__ == '__main__':
    app.run(debug=True)