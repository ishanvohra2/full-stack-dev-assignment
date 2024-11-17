from flask import Flask, request, jsonify
from flask_cors import CORS
from firebase_admin import auth
from config import firebase_app

app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(debug=True)