// src/services/api.ts
import axios from 'axios';

// URL base da sua API
const API_BASE_URL = 'http://localhost:8000'; // Altere conforme necessario

// Função para obter o token do localStorage
const getToken = (): string | null => {
    return localStorage.getItem('token');
};

// Criando a instância do axios
const api = axios.create({
    baseURL: API_BASE_URL,
});

// Adicionando o token de forma automática nos headers
api.interceptors.request.use(
    (config) => {
        const token = getToken();
        if (token) {
        // Adiciona o token no cabeçalho de autorização se ele existir
        config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;