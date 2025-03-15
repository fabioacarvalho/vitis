// src/services/userService.ts
import api from './api';

// Função para obter a lista de usuários
const getUsers = async () => {
    try {
        const data = await api.get('/users/');
        return data;
    } catch (error) {
        console.error('Failed to fetch users:', error);
        throw error;
    };
};

// Função para obter um usuário por ID
const getUserById = async (id: number) => {
    try {
        const data = await api.get(`/users/${id}/`);
        return data;
    } catch (error) {
        console.error('Failed to fetch users:', error);
        throw error;
    };
};

const createUser = async (payload: any) => {
    try {
        const data = await api.post(`/core/companies/`, payload);
        return data;
    } catch (error) {
        console.error('Failed to create company:', error);
        throw error;
    };
};

const updateUser = async (id: number, payload: any) => {
    try {
        const data = await api.post(`/core/companies/${id}`, payload);
        return data;
    } catch (error) {
        console.error('Failed to update company:', error);
        throw error;
    };
};

const deleteUser = async (id: any) => {
    try {
        const data = await api.delete(`/core/companies/${id}`);
        return data;
    } catch (error) {
        console.error('Failed to delete company:', error);
        throw error;
    };
};

const userService = {
    getUsers,
    getUserById,
    createUser,
    updateUser,
    deleteUser,
};

export default userService;