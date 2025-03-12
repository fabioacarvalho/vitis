import styled from "styled-components";

export const TableStyle = styled.table`
    width: 100%;
    border-collapse: collapse;
    border: none;

    th {
        background-color: ${props => props.theme.colors.gray};
    }
    
    th:first-child {
        border-radius: 8px 0 0 0;
    }
    
    th:last-child {
        border-radius: 0 8px 0 0;
    }

    /* tr:nth-child(even) {
        background-color: ${(props) => props.theme.colors.shadow_gray};  // Cor para as linhas ímpares
    } */

    
    tr {
        border-bottom: 1px solid ${props => props.theme.colors.shadow_blue};
    }

    tr, td {
        min-height: 40px;
        height: 40px;
    }

    tr:hover > td {
        background-color: ${(props) => props.theme.colors.shadow_blue};
    }

    td {
        padding: 0 0 0 10px;
        text-align: center;
    }

    .actions {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
    }
  
`;

export const ContainerActionsTable = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
`;

export const FilterTable = styled.div`
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 5px;
`;

export const InputField = styled.input`
    padding: 10px;
    border-radius: 8px;
    border: 1px solid ${props => props.theme.colors.shadow_gray};
    color: ${props => props.theme.colors.black};

    &:hover {
        border: 1px solid ${props => props.theme.colors.gray};
    }
`;

export const Footer = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    gap: 10px;
`;

export const Box = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    height: 15vh;
    border: 1px dashed #C1C1C1;
    border-radius: 8px;
    color: #C1C1C1;
    text-align: center;

`;