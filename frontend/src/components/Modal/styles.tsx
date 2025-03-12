import styled from "styled-components";

export const ModalOverlay = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Fundo escuro semitransparente */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
`;

interface ModalContentProps { 
    theme: any; 
}

export const ModalContent = styled.div<ModalContentProps>`
    background: #fff; /* Cor de fundo do modal */
    border-radius: 8px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    width: 90%;
    max-width: 80vw; /* Tamanho máximo do modal */
    padding: 20px;
    animation: fadeIn 0.3s ease-in-out;

    .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;

        h1 {
            font-size: 1.5rem;
            margin: 0;
        }

        .close-btn {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #333;
            transition: color 0.2s;

            &:hover {
                color: red;
            }
        }
    }

    .modal-body {
        font-size: 1rem;
        color: #444;
    }

    .modal-footer {
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;

        button {
            padding: 8px 16px;
            font-size: 1rem;
            border: none;
            border-radius: 4px;
            background: ${props => props.theme.colors.blue};
            color: #fff;
            cursor: pointer;
            transition: background 0.2s;

            &:hover {
                background: ${props => props.theme.colors.gray};
                color: ${props => props.theme.colors.blue};
            }

            & + button {
                margin-left: 8px;
            }
        }
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
`;