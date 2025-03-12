import React from 'react';
import { HeaderStyle, ToggleButton, ButtonSettings } from './styles';
import { useMenu } from '../../contexts/MenuContext';
import { FaUserLarge } from "react-icons/fa6";
import { FaBars, FaAnglesLeft } from "react-icons/fa6";

export const Header = () => {
    const { isCollapsed, toggleCollapse } = useMenu();

    return (
        <HeaderStyle isCollapsed={isCollapsed}>
            <div style={{ display: 'flex', alignItems: 'center', }}>
                {isCollapsed ? (
                    <ToggleButton onClick={() => toggleCollapse()}>
                        <FaBars size={22} color='#0592f0' />
                    </ToggleButton>
                ) : (
                    <ToggleButton onClick={() => toggleCollapse()}>
                        <FaAnglesLeft size={22} color='#0592f0'/>
                    </ToggleButton>
                )}
                <h1 style={{ marginLeft: 15, }}>Logo</h1>
            </div>

            <ButtonSettings onClick={() => alert("Settings user")}>
                <FaUserLarge  />
                <span style={{ marginLeft: 10, }}>Settings</span>
            </ButtonSettings>
        </HeaderStyle>
    );
};