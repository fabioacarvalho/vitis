import React, { createContext, useContext, ReactNode, useState } from "react";
import { Theme, lightTheme, darkTheme } from "../types/theme"; // Importando o tipo e os temas

// Criando o contexto do tema
const ThemeContext = createContext<{
  theme: Theme;
  toggleTheme: () => void;
} | undefined>(undefined);

interface ThemeProviderProps {
  children: ReactNode;
}

export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children }) => {
  const [theme, setTheme] = useState<Theme>(lightTheme); // Definindo o estado do tema

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === lightTheme ? darkTheme : lightTheme)); // Alternando entre o tema claro e escuro
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

// Hook para acessar o tema em qualquer componente
export const useTheme = (): { theme: Theme; toggleTheme: () => void } => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
};