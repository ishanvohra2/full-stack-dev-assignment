class ApiService {
    constructor() {
        this.baseUrl = 'https://language-learning-app-backend.vercel.app/api';
    }

    // Helper method for handling fetch responses
    async handleResponse(response) {
        if (!response.ok) {
            const error = await response.json();
            console.log("API FAILED", error)
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
}

// Create a singleton instance
const apiService = new ApiService();
export default apiService;