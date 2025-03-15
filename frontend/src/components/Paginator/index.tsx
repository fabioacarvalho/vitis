import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { FaChevronLeft, FaChevronRight } from "react-icons/fa6";
import { Button } from '../Button';
import { PaginatorStyle } from './styles';

interface PaginatorProps {
    currentPage: number; // Página atual
    totalPages: number; // Total de páginas
    onPageChange: (page: number) => void; // Função chamada ao mudar a página
}

const Paginator: React.FC<PaginatorProps> = ({ currentPage, totalPages, onPageChange }) => {
    const { theme } = useTheme();

    const handlePrevious = () => {
        if (currentPage > 1) {
            onPageChange(currentPage - 1);
        }
    };

    const handleNext = () => {
        if (currentPage < totalPages) {
            onPageChange(currentPage + 1);
        }
    };

    const handlePageClick = (page: number) => {
        onPageChange(page);
    };

    return (
        <PaginatorStyle>
            <Button name={<FaChevronLeft color={theme.colors.blue} />} onClick={handlePrevious} disabled={currentPage === 1} className='btn btn-icon'/>

            {Array.from({ length: totalPages }).map((_, index) => (
                <Button
                    key={index}
                    name={index + 1}
                    className='btn btn-primary'
                    onClick={() => handlePageClick(index + 1)}
                    style={{
                        backgroundColor: currentPage === index + 1 ? theme.colors.blue : 'transparent',
                        color: currentPage === index + 1 ? 'white' : theme.colors.black,
                        margin: '0 5px',
                    }}
                />
            ))}

            <Button name={<FaChevronRight color={theme.colors.blue} />} onClick={handleNext} disabled={currentPage === totalPages} className='btn btn-icon'/>
        </PaginatorStyle>
    );
};

export default Paginator;