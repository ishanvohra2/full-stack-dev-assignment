import os
from firebase_admin import credentials, initialize_app

# Firebase configuration
cred = credentials.Certificate("firebase_config.json")
firebase_app = initialize_app(cred)