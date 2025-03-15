import React, { useState } from 'react';
import { SidebarContainer, SidebarContent, SidebarItem, SidebarFooter, SubItems } from './styles';
import { FaArrowRightFromBracket, FaComments, FaChevronDown, FaChevronUp } from "react-icons/fa6";
import { useMenu } from '../../contexts/MenuContext';
import menu from "../../types/menu"; // Importa a lista de menus
import { useNavigate, Link } from "react-router-dom";

export const Sidebar: React.FC = () => {
    const { isCollapsed } = useMenu();
    const [openGroups, setOpenGroups] = useState<{ [key: string]: boolean }>({});
    const navigate = useNavigate();

    // Função para alternar o estado de um grupo
    const toggleGroup = (group: string) => {
        setOpenGroups(prevState => ({
            ...prevState,
            [group]: !prevState[group],
        }));
    };

    const signOut = () => {
        localStorage.removeItem("token");
        navigate("/sign-in");
    };

    return (
        <SidebarContainer isCollapsed={isCollapsed}>
            <SidebarContent>
            {menu
                .filter((item) => !item.sub_group) // Renderiza apenas itens principais (sem sub_group)
                .map((item, index) => {
                const isGroup = menu.some((subItem) => subItem.group === item.group && subItem.sub_group);
                const isOpen = openGroups[item.group];

                return (
                    <React.Fragment key={index}>
                    {/* Item Principal */}
                    <SidebarItem
                        isCollapsed={isCollapsed}
                        onClick={() => {
                        if (isGroup) {
                            toggleGroup(item.group); // Abre ou fecha o grupo
                        } else {
                            navigate(item.path)
                        }
                        }}
                    >
                        <div className="content-item">
                        {item.icon}
                        {!isCollapsed && <div>{item.name}</div>}
                        {isGroup && !isCollapsed && (isOpen ? <FaChevronUp /> : <FaChevronDown />)}
                        </div>
                    </SidebarItem>

                    {/* Subitens */}
                    {isGroup && isOpen && !isCollapsed && (
                        <SubItems>
                        {menu
                            .filter((subItem) => subItem.group === item.group && subItem.sub_group)
                            .map((subItem) => (
                            <SidebarItem
                                isCollapsed={isCollapsed}
                                key={subItem.id}
                                onClick={() => navigate(`${item.path}${subItem.path}`)}
                            >
                                <div className="content-item">
                                {subItem.icon}
                                {!isCollapsed && <div>{subItem.name}</div>}
                                </div>
                            </SidebarItem>
                            ))}
                        </SubItems>
                    )}
                    </React.Fragment>
                );
                })}
            </SidebarContent>

            {/* Footer of Menu */}
            <SidebarFooter>
                <SidebarContent>
                    <SidebarItem isCollapsed={isCollapsed} onClick={() => navigate("/help")}>
                        <div className='content-item'>
                            <FaComments />
                            {!isCollapsed && (<div>Help</div>)}
                        </div>
                    </SidebarItem>
                    <SidebarItem isCollapsed={isCollapsed} onClick={() => signOut()}>
                        <div className='content-item'>
                            <FaArrowRightFromBracket />
                            {!isCollapsed && (<div>Sign-out</div>)}
                        </div>
                    </SidebarItem>
                </SidebarContent>

            </SidebarFooter>
        </SidebarContainer>
    );
};
