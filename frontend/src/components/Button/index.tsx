import React from 'react';
import { ButtonStyled } from './styles';

interface ButtonProps {
    className?: string;
    name: string | React.ReactNode;
    onClick?: () => void;
    type?: string;
    otherProps?: any[];
};

export const Button = ({name, className, onClick, type, otherProps}: ButtonProps) => {
    return (
        <ButtonStyled 
        className={className}
        onClick={onClick}
        type={type}
        {...otherProps}
        >{name}</ButtonStyled>
    );
}