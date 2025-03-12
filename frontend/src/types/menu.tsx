import React from "react";
import { FaHeadSideVirus, FaScrewdriverWrench, FaArrowTrendUp, FaHouseChimney, FaRegRectangleList, FaRegUser, FaSeedling, FaRuler, FaSliders, FaBusSimple, FaCarBattery, FaBacterium, FaBuilding, FaCarrot, FaDiceOne, FaDiceTwo, FaDiceThree } from "react-icons/fa6";

interface MenuProps {
    id: number;
    name: string;
    path: string;
    super_user: boolean;
    admin: boolean;
    icon: React.ReactNode;
    sub_group: boolean;
    group: string;
};

const menu = [
    {
        id: 1, 
        name: 'Home', 
        path: '/', 
        super_user: false, 
        admin: false, 
        icon: <FaHouseChimney />, 
        sub_group: false, 
        group: ''
    },{
        id: 2, 
        name: 'Dashboard', 
        path: '/dashboard', 
        super_user: false, 
        admin: false, 
        icon: <FaArrowTrendUp />, 
        sub_group: false, 
        group: ''
    },{
        id: 3, 
        name: 'Items', 
        path: '/items', 
        super_user: false, 
        admin: false, 
        icon: <FaRegRectangleList />, 
        sub_group: false, 
        group: ''
    },{
        id: 4, 
        name: 'Settings', 
        path: '/settings', 
        super_user: false, 
        admin: true, 
        icon: <FaScrewdriverWrench />, 
        sub_group: false, 
        group: 'settings'
    },{
        id: 5, 
        name: 'Users', 
        path: '/users', 
        super_user: false, 
        admin: true, 
        icon: <FaRegUser />, 
        sub_group: true, 
        group: 'settings'
    },{
        id: 6, 
        name: 'Company', 
        path: '/company', 
        super_user: true, 
        admin: true, 
        icon: <FaBuilding />, 
        sub_group: true, 
        group: 'settings'
    }
] as MenuProps[];

export default menu;
