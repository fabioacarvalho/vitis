import api from './api';


class EntityService {
    private route: string;

    constructor(route: string) {
        this.route = route;
    }

    async get() {
        try {
            const response = await api.get(this.route);
            return response.data;
        } catch (error) {
            throw new Error(`Error fetching data: ${error}`);
        }
    }

    async getById(id: string) {
        try {
            const response = await api.get(`${this.route}/${id}`);
            return response.data;
        } catch (error) {
            throw new Error(`Error fetching data by id: ${error}`);
        }
    }

    async create(data: any) {
        try {
            const response = await api.post(this.route, data);
            return response.data;
        } catch (error) {
            throw new Error(`Error creating data: ${error}`);
        }
    }

    async update(id: string, data: any) {
        try {
            const response = await api.put(`${this.route}/${id}`, data);
            return response.data;
        } catch (error) {
            throw new Error(`Error updating data: ${error}`);
        }
    }

    async delete(id: string) {
        try {
            const response = await api.delete(`${this.route}/${id}`);
            return response.data;
        } catch (error) {
            throw new Error(`Error deleting data: ${error}`);
        }
    }
}

// example use:
// export const CompanyService = new EntityService('/api/companies');

export default EntityService;