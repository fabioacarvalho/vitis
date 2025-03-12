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
        name: 'Parameters', 
        path: '/parameters', 
        super_user: false, 
        admin: true, 
        icon: <FaSliders />, 
        sub_group: false, 
        group: 'parameters'
    },{
        id: 7, 
        name: 'Emission Factors', 
        path: '/emission-factors', 
        super_user: false, 
        admin: true, 
        icon: <FaSeedling />, 
        sub_group: true, 
        group: 'parameters'
    },{
        id: 8, 
        name: 'Variable Factors', 
        path: '/parameters/home-work', 
        super_user: false, 
        admin: true, 
        icon: <FaRuler />, 
        sub_group: true, 
        group: 'parameters'
    },{
        id: 9, 
        name: 'Conversion Factors', 
        path: '/parameters/home-work', 
        super_user: false, 
        admin: true, 
        icon: <FaHeadSideVirus />, 
        sub_group: true, 
        group: 'parameters'
    },{
        id: 10, 
        name: 'Scope 1', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaDiceOne />, 
        sub_group: false, 
        group: 'scope1'
    },{
        id: 11, 
        name: 'Scope 2', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaDiceTwo />, 
        sub_group: false, 
        group: 'scope2'
    },{
        id: 12, 
        name: 'Scope 3', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaDiceThree />, 
        sub_group: false, 
        group: 'scope3'
    },{
        id: 13, 
        name: 'Stationary Combustion', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaCarBattery />, 
        sub_group: true, 
        group: 'scope1'
    },{
        id: 14, 
        name: 'Mobile Combustion', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaBusSimple />, 
        sub_group: true, 
        group: 'scope1'
    },{
        id: 15, 
        name: 'Fugitive Emissions', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaBacterium />, 
        sub_group: true, 
        group: 'scope1'
    },{
        id: 16, 
        name: 'Industrial Processes', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaBuilding />, 
        sub_group: true, 
        group: 'scope1'
    },{
        id: 17, 
        name: 'Agricultural Activities', 
        path: '', 
        super_user: false, 
        admin: false, 
        icon: <FaCarrot />, 
        sub_group: true, 
        group: 'scope1'
    },{
        id: 18, 
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
