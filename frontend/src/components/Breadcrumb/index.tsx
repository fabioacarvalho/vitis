import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BreadcrumbContainer } from "./styles"
import { useTheme } from '../../contexts/ThemeContext';
import { FaChevronRight } from "react-icons/fa6";

const Breadcrumb = () => {
    const location = useLocation();
    const pathnames = location.pathname.split('/').filter((x) => x);
    const { theme } = useTheme();

    return (
        <BreadcrumbContainer aria-label="breadcrumb" theme={theme}>
            <ul className="breadcrumb">
                <li>
                    <Link to="/" className="link">Home </Link> 
                </li>
                {pathnames.map((value, index) => {
                    const to = `/${pathnames.slice(0, index + 1).join('/')}`;
                    const isLast = index === pathnames.length - 1;

                    return (
                        <li key={to} className={isLast ? "current" : undefined}>
                            {isLast ? (
                                <span style={{display: 'flex', alignItems: 'center', gap: 5,}}> <FaChevronRight color={theme.colors.black} size={14}/> {value}</span>
                            ) : (
                                <Link to={to} className="link"> {value}</Link>
                                
                            )}
                        </li>
                        // <li key={to} className={isLast ? "current" : undefined}>
                        //     {isLast ? (
                        //         value
                        //     ) : (
                        //         <Link to={to} className="link">{value}</Link>
                        //     )}
                        // </li>
                    );
                })}
            </ul>
        </BreadcrumbContainer>
    );
};

export default Breadcrumb;