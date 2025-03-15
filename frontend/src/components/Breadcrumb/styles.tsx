import styled from "styled-components";

export const BreadcrumbContainer = styled.nav`
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    color: ${props => props.theme.colors.black};

    .breadcrumb {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .link {
        text-decoration: none;
        color: '#007bff';
        margin-right: 10px;
    }
    .current {
        color: '#6c757d';
    }
`;