import styled from 'styled-components';

export const SidebarContainer = styled.div<{ isCollapsed: boolean }>`
    width: ${props => (props.isCollapsed ? '80px' : '260px')};
    height: 100%; /* Garante que o sidebar ocupa toda a altura disponível */
    /* background-color: #dcdcdc; */
    border-right: 1px solid #e6f4ff;
    color: #1677ff;
    transition: width 0.3s;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box; /* Garante que padding não cause overflow */
    overflow: hidden; /* Evita scrollbars internas no sidebar */
`;

export const ToggleButton = styled.button`
    background-color: #444;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    margin-top: 10px;
`;

export const SidebarContent = styled.div`
    margin-top: 20px;
    width: 100%;
    text-align: center;
`;

export const SidebarFooter = styled.div`
    margin-top: 20px;
    width: 100%;
    height: 150px;
    text-align: center;
`;

export const SidebarItem = styled.div<{ isCollapsed: boolean }>`
    color: #1677ff;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin: 5px 10px;

    cursor: pointer;
    padding: 10px;
    border-radius: 5px;

    &:hover {
        background-color: rgba(237, 237, 237, 0.733);
    }

    &:active {
        transform: scale(0.98);
        background-color: #e6f4ff;
        color: #1677ff;
    }

    .content-item {
        display: flex;
        align-items: center;
        justify-content: ${props => (props.isCollapsed ? 'center' : 'flex-start')};
        gap: ${props => (props.isCollapsed ? '0' : '10px')};
        width: 100%;
    }
`;

export const SubItems = styled.div`
    margin: 10px;
    margin-top: 5px;
    text-align: left;
    color: #1677ff;

    div {
        cursor: pointer;

        &:hover {
            background-color: rgba(237, 237, 237, 0.734);
        }
    }
`;