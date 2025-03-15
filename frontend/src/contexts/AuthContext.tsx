import React, { createContext, useState, useEffect } from "react";
import authService from "../services/authService";

interface AuthContextProps {
    user: any;
    login: (username: string, password: string) => Promise<void>;
    logout: () => void;
    isAuthenticated: boolean;
}

export const AuthContext = createContext<AuthContextProps | null>(null);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [user, setUser] = useState<any>(null);
    const [loading, setLoading] = useState<boolean>(true); // Para lidar com a sincronização

    function debugTrue() {

        let user = {username: "admin", email: "admin@admin.com"}
        let token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMDE3NDA4LCJpYXQiOjE3NDEwMTcxMDgsImp0aSI6IjczMmU2YjIxNjk5ODQ3YjFiYmJmZGFhY2U0NzAxYTJjIiwidXNlcl9pZCI6MX0.tOG4SS7b_6JGmgiD2WYY_UQsLSVudFcJ39kJtGP73go"
        setUser({token: token, user: user})
        localStorage.setItem("user", JSON.stringify(user));
        localStorage.setItem("token", token);
    }

    useEffect(() => {
        // Verificando se há usuário e token no localStorage
        const storedUser = localStorage.getItem("user");
        const storedToken = localStorage.getItem("token");

        // Apenas em DEBUG TRUE
        // debugTrue()
        
        if (storedUser && storedToken) {
            try {
                // Restaurando o estado do usuário
                setUser(JSON.parse(storedUser));
                // Aqui você pode adicionar uma verificação para o token, se necessário
            } catch (e) {
                console.error("Error parsing user from localStorage", e);
                localStorage.removeItem("user");
                localStorage.removeItem("token");
                setUser(null);
            }
        }
        setLoading(false); // Após verificar e definir o estado, desativa o loading
    }, []);

    const login1 = async (username: string, password: string) => {
        try {
            if (!username || !password) {
                throw new Error("Username and password are required");
            }

            const response = await fetch("http://127.0.0.1:8000/login/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error("Invalid credentials");
            }

            const data = await response.json();
            if (!data || !data.user || !data.token) {
                throw new Error("Invalid response data");
            }

            setUser(data.user);
            localStorage.setItem("user", JSON.stringify(data.user));
            localStorage.setItem("token", data.token);

            return true;
        } catch (error) {
            console.error(error);
            alert("Login failed: " + error.message);
        }
    };

    const login = async (username: string, password: string) => {
        try {
            if (!username || !password) {
                throw new Error("Username and password are required");
            }
    
            const response = await authService.signIn(username, password);
            console.log(response);
    
            if (!response.data || !response.data.user || !response.data.token) {
                throw new Error("Invalid response data");
            }
    
            const { user, token } = response.data;
    
            setUser(user);
            localStorage.setItem("user", JSON.stringify(user));
            localStorage.setItem("token", token);
    
            return true;
        } catch (error) {
            console.error(error);
            alert("Login failed: " + error.message);
            return false;
        }
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem("user");
        localStorage.removeItem("token");
    };

    // Verificando se o usuário está autenticado
    const isAuthenticated = Boolean(user);

    // Se estiver carregando, pode mostrar um loading ou redirecionar para o login
    if (loading) {
        return <div>Loading...</div>; // Aqui você pode exibir uma tela de carregamento
    }

    return (
        <AuthContext.Provider value={{ user, login, logout, isAuthenticated }}>
            {children}
        </AuthContext.Provider>
    );
};