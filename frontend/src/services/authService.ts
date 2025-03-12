import api from './api';

const signIn = async (username: string, password: string) => {
    try {
        const response = await api.post('sign-in/', {
            username: username,
            password: password,
        });
        return response;
    } catch (error) {
        console.error('Failed to sign in:', error);
        throw error;
    }
};

const authService = {
    signIn,
};

export default authService;