# Language Learning Application

A full-stack language learning platform built with Svelte and Flask.

## Tech Stack

### Frontend
- Svelte v5.0.0
- SvelteKit v2.0.0
- Firebase v11.0.2
- Lottie-web v5.12.2
### Backend
- Flask v3.1.0
- Firebase Admin v5.0.0
- Python-dotenv v0.19.0
- Flask-CORS v3.0.10

## Prerequisites
- Node.js (Latest LTS version)
- Python 3.8+
- Firebase account and project setup
- Git

## Setup Instructions

1. Clone the repository

`git clone https://github.com/ishanvohra2/full-stack-dev-assignment.git
cd full-stack-dev-assignment`

2. Frontend Setup

`# Navigate to frontend directory
cd language-learning-app-frontend

# Install dependencies
npm install

# Create firebase config
# Create src/lib/firebaseConfig.json with your Firebase credentials:
{
  "apiKey": "your-api-key",
  "authDomain": "your-auth-domain",
  "projectId": "your-project-id",
  "storageBucket": "your-storage-bucket",
  "messagingSenderId": "your-messaging-sender-id",
  "appId": "your-app-id"
}

# Start development server
npm run dev`

3. Backend Setup
`# Navigate to backend directory
cd language-learning-app-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with Firebase admin credentials
# Add your Firebase admin SDK JSON content

# Start Flask server
python app.py`

## Firebase setup
1. Firebase Setup
2. Create a new Firebase project
3. Enable Authentication (Google Sign-in)
4. Set up Firestore Database
5. Download Firebase Admin SDK credentials
6. Add Firebase configuration to frontend
7. Set up Firebase Admin SDK in backend
