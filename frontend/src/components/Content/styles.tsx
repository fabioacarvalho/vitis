import styled from "styled-components";

interface ContentStyleProps {
    isCollapsed: boolean;
}

export const ContentStyle = styled.div<ContentStyleProps>`
    flex-grow: 1; /* Permite que o conteúdo preencha o espaço restante */
    overflow-y: auto; /* Garante que o scroll só aparece quando necessário */
    margin: 0;
    padding: 10px;
    box-sizing: border-box; /* Inclui padding no cálculo do tamanho */
    height: 100%;
`;