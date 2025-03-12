import React, { createContext, useContext, useState, ReactNode } from 'react';

interface MenuContextProps {
    isCollapsed: boolean;
    toggleCollapse: () => void;
}

const MenuContext = createContext<MenuContextProps | undefined>(undefined);

export const MenuProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [isCollapsed, setIsCollapsed] = useState(false);

    const toggleCollapse = () => {
        setIsCollapsed(prevState => !prevState);
    };

    return (
        <MenuContext.Provider value={{ isCollapsed, toggleCollapse }}>
            {children}
        </MenuContext.Provider>
    );
};

export const useMenu = (): MenuContextProps => {
    const context = useContext(MenuContext);
    if (!context) {
        throw new Error('useMenu must be used within a MenuProvider');
    }
    return context;
};

