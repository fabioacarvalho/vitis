import styled from "styled-components";

interface ContainerFormProps {
    columns: number;
    theme? : any;
}

export const ContainerForm = styled.form<ContainerFormProps>`
    display: grid;
    grid-template-columns: repeat(${(props) => props.columns ? props.columns : 3}, 1fr); /* Define o número de colunas */
    gap: 16px; /* Espaço entre os campos */
    width: 100%;

    .form-group {
        display: flex;
        flex-direction: column;
        grid-column: span 1; /* Garantir que cada campo ocupe uma célula */
        
        label {
            font-size: 14px;
            font-weight: 500;
            color: ${props => props.theme.colors.black}; /* Cor do label */
            margin-bottom: 8px;
        }

        input {
            padding: 8px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
    }
`;