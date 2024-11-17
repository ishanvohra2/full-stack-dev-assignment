import { writable } from 'svelte/store';

function createAuthStore() {
    const { subscribe, set, update } = writable({
        user: null,
        token: null,
        loading: true
    });

    return {
        subscribe,
        setUser: (user, token) => {
            if (token) {
                localStorage.setItem('authToken', token);
            }
            set({ user, token, loading: false });
        },
        clearUser: () => {
            localStorage.removeItem('authToken');
            set({ user: null, token: null, loading: false });
        },
        setLoading: (loading) => update(state => ({ ...state, loading }))
    };
}

export const authStore = createAuthStore();