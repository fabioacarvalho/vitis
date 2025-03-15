// src/contexts/AppProvider.tsx
import React from "react";
import { MenuProvider } from "./MenuContext";
import { AuthProvider } from "./AuthContext";
import { ThemeProvider } from "./ThemeContext";

interface AppProviderProps {
    children: React.ReactNode;
}

const AppProvider: React.FC<AppProviderProps> = ({ children }) => {
    return (
        <AuthProvider>
            <ThemeProvider>
                <MenuProvider>
                    {children}
                </MenuProvider>
            </ThemeProvider>
        </AuthProvider>
    );
};

export default AppProvider;