class ApiService {
    constructor() {
        this.baseUrl = 'https://language-learning-app-backend.vercel.app/api';
    }

    async refreshToken() {
        const currentUser = auth.currentUser;
        if (currentUser) {
            try {
                const newToken = await currentUser.getIdToken(true); // Force token refresh
                localStorage.setItem('authToken', newToken);
                return newToken;
            } catch (error) {
                console.error('Failed to refresh token:', error);
                throw error;
            }
        }
        throw new Error('No user logged in');
    }

    // Helper method for handling fetch responses
    async handleResponse(response) {
        if (response.status === 401) {
            try {
                // Try to refresh token
                const newToken = await this.refreshToken();
                // Retry the original request with new token
                const retryResponse = await fetch(response.url, {
                    ...response,
                    headers: {
                        ...response.headers,
                        'Authorization': `Bearer ${newToken}`
                    }
                });
                if (!retryResponse.ok) {
                    throw new Error('Request failed after token refresh');
                }
                return retryResponse.json();
            } catch (error) {
                throw error;
            }
        }
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.message || 'API request failed');
        }
        return response.json();
    }

    // Get auth token from localStorage
    getAuthToken() {
        return localStorage.getItem('authToken');
    }

    // Verify Google token
    async verifyGoogleToken(token) {
        try {
            const response = await fetch(`${this.baseUrl}/auth/verify-token`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ token })
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Token verification failed:', error);
            throw error;
        }
    }

    // Get user profile
    async getUserProfile() {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/user/profile`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Failed to fetch user profile:', error);
            throw error;
        }
    }

    async getLanguages() {
        try {
            const response = await fetch(`${this.baseUrl}/languages`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Failed to fetch languages:', error);
            throw error;
        }
    }

    // Create user profile
    async createUserProfile(languages) {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/user/create-profile`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ languages })
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Failed to create profile:', error);
            throw error;
        }
    }

    async getOnboardingQuestions() {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/onboarding/questions`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Failed to fetch onboarding questions:', error);
            throw error;
        }
    }

    async saveOnboardingAnswers(answers) {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/onboarding/save`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ answers })
            });
            return this.handleResponse(response);
        } catch (error) {
            if (error.message.includes('Token expired')) {
                // Token expired error will be handled by handleResponse
                throw error;
            }
            console.error('Failed to save onboarding answers:', error);
            throw error;
        }
    }

    async checkOnboardingStatus() {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/user/check-onboarding`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Failed to check onboarding status:', error);
            throw error;
        }
    }

    async addLanguage(languageData) {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/user/add-language`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(languageData)
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Failed to add language:', error);
            throw error;
        }
    }

    async getLessons(language) {
        try {
            const response = await fetch(`${this.baseUrl}/lessons/${language}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                }
            });
    
            if (!response.ok) {
                throw new Error('Failed to fetch lessons');
            }
    
            return await response.json();
        } catch (error) {
            console.error('Error fetching lessons:', error);
            throw error;
        }
    }

    async completeLesson(type, id) {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/user/complete-lesson`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ type, id })
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Error completing lesson:', error);
            throw error;
        }
    }

    async updateLessonProgress(lessonType, lessonId) {
        try {
            const token = this.getAuthToken();
            const response = await fetch(`${this.baseUrl}/user/complete-lesson`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    type: lessonType,
                    id: lessonId
                })
            });
            return this.handleResponse(response);
        } catch (error) {
            console.error('Error updating lesson progress:', error);
            throw error;
        }
    }
}

// Create a singleton instance
const apiService = new ApiService();
export default apiService;