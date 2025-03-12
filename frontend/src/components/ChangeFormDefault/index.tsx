import React from "react";
import { ContainerForm } from "./styles";
import { useTheme } from "../../contexts/ThemeContext";


interface ChangeFormProps {
    children: React.ReactNode;
    columns: number
    onSubmit?: () => void;
}

const ChangeFormDefault = ({ children, columns, onSubmit }: ChangeFormProps) => {
    const { theme } = useTheme();
    return (
        <ContainerForm onSubmit={onSubmit} theme={theme} columns={columns}>
            {children}
            <input type="submit" value="Save" />
        </ContainerForm>
    );
};

export default ChangeFormDefault;
