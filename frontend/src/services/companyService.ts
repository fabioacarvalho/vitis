import api from './api';


const getCompanyById = async (id: number) => {
    try {
        const data = await api.get(`/core/companies/${id}/`);
        return data;
    } catch (error) {
        console.error('Failed to fetch company:', error);
        throw error;
    };
};

const getCompanys = async () => {
    try {
        const data = await api.get(`/core/companies/`);
        return data;
    } catch (error) {
        console.error('Failed to fetch company:', error);
        throw error;
    };
};

interface CompanyProps {
    name: string;
    cnpj: string;
    phone: string;
    email: string;
    cep: string;
    code: string;
    country: string;
    state: string;
    city: string;
    address: string;
    message?: string;
}

const createCompany = async (payload: any) => {
    try {
        const data = await api.post(`/core/companies/create/`, payload);
        return data;
    } catch (error) {
        console.error('Failed to create company:', error);
        throw error;
    };
};

const updateCompany = async (id: number, payload: any) => {
    try {
        const data = await api.post(`/core/companies/update/${id}`, payload);
        return data;
    } catch (error) {
        console.error('Failed to update company:', error);
        throw error;
    };
};

const deleteCompany = async (id: number) => {
    try {
        const data = await api.delete(`/core/companies/delete/${id}`);
        return data;
    } catch (error) {
        console.error('Failed to delete company:', error);
        throw error;
    };
};

const companyService = {
    getCompanyById,
    getCompanys,
    createCompany,
    updateCompany,
    deleteCompany,
};

export default companyService;