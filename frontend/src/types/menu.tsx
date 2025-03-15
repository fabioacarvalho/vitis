import React from "react";
import { FaScrewdriverWrench, FaArrowTrendUp, FaHouseChimney, FaRegRectangleList, FaRegUser, FaBuilding, FaRightLeft } from "react-icons/fa6";

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
        name: 'Pipeline', 
        path: '/pipeline', 
        super_user: false, 
        admin: false, 
        icon: <FaRightLeft />, 
        sub_group: false, 
        group: ''
    },{
        id: 4, 
        name: 'Items', 
        path: '/items', 
        super_user: false, 
        admin: false, 
        icon: <FaRegRectangleList />, 
        sub_group: false, 
        group: ''
    },{
        id: 5, 
        name: 'Settings', 
        path: '/settings', 
        super_user: false, 
        admin: true, 
        icon: <FaScrewdriverWrench />, 
        sub_group: false, 
        group: 'settings'
    },{
        id: 6, 
        name: 'Users', 
        path: '/users', 
        super_user: false, 
        admin: true, 
        icon: <FaRegUser />, 
        sub_group: true, 
        group: 'settings'
    },{
        id: 7, 
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
