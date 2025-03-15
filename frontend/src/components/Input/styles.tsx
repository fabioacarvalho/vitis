import styled from "styled-components";

export const InputField = styled.input`
    padding: 10px;
    border-radius: 8px;
    border: 1px solid ${props => props.theme.colors.shadow_gray};
    color: ${props => props.theme.colors.black};

    &:hover {
        border: 1px solid ${props => props.theme.colors.gray};
    }
`;