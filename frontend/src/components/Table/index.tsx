import React, { useEffect, useState } from "react";
import { TableStyle, ContainerActionsTable, FilterTable, Footer, Box } from './styles'
// import theme from "../../types/theme";
import { useTheme } from '../../contexts/ThemeContext'; // Usando o hook para acessar o tema
import { FaRegTrashCan, FaRegPenToSquare, FaRegSquarePlus, } from "react-icons/fa6";
import { Button } from "../Button";
import Input from "../Input";
import Paginator from "../Paginator";
import { useNavigate, useLocation } from "react-router-dom";
import { NavigateChangeFormProps } from "../../types/interfaces";


// Tipagem para os dados da tabela
interface TableData {
    [key: string]: string | number;
}

interface TableProps {
    columns: string[]; // Cabeçalhos da tabela
    data: TableData[]; // Dados da tabela
    state?: NavigateChangeFormProps;
}

const Table: React.FC<TableProps> = ({ columns, data, state }) => {
    const navigate = useNavigate();
    const { theme } = useTheme();
    const [tableData, setTableData] = useState<TableData[]>(data);
    const [currentPage, setCurrentPage] = useState(1);
    const location = useLocation();

    // Calculando o total de páginas
    const totalPages = Math.ceil(data.length / 10);

    // Calculando os dados da página atual
    const currentData = data.slice((currentPage - 1) * 10, currentPage * 10);

    const handleAddRow = () => {
        const context = location.pathname
        console.log("Navegando para:", `${context}/add`); // Log para depuração
        if (context) { // Verifica se o contexto está definido
            navigate(`${context}/add`);
        } else {
            console.error("Contexto não definido.");
        }
    };


    const handlePageChange = (page: number) => {
        setCurrentPage(page);
    };

    const handleChange = (rowIndex: number, columnName: string, value: string | number) => {
        const updatedData = [...tableData];
        updatedData[rowIndex] = {
            ...updatedData[rowIndex],
            [columnName]: value,
        };
        setTableData(updatedData);
    };

    const handleFilter = () => {

    };

    const handleDeleteRow = (rowIndex: number) => {
        const updatedData = tableData.filter((_, index) => index !== rowIndex);
        setTableData(updatedData);
    };

    useEffect(() => {
        setTableData(data)
    }, [data]);

    return (
        <div>

            <ContainerActionsTable theme={theme}>
                <FilterTable theme={theme}>
                    <Input placeholder="ID" type="text"/>
                    <Input placeholder="Name" type="text"/>
                    <Button className="btn btn-thirdary" name="Filter" onClick={() => handleFilter()}/>
                </FilterTable>
                <Button className="btn btn-icon" onClick={handleAddRow} name={<FaRegSquarePlus color={theme.colors.blue} size={22}/>} />
            </ContainerActionsTable>
            
            {tableData.length ? (
                <>
                    <TableStyle theme={theme}>

                        <thead>
                            <tr>
                                {columns.map((column) => (
                                    <th key={column}>{column}</th>
                                ))}
                                <th>Actions</th>
                            </tr>
                        </thead>

                        <tbody>
                            {tableData.map((row, rowIndex) => (
                                <tr key={rowIndex}>
                                    {columns.map((column) => (
                                        <td key={column}>
                                            {row[column] || "-"}
                                        </td>
                                    ))}
                                    <td className="actions">
                                        <Button 
                                            name={<FaRegTrashCan color={theme.colors.danger} />}
                                            className="btn btn-icon"
                                            onClick={() => handleDeleteRow(rowIndex)}
                                        />
                                        <Button
                                            name={<FaRegPenToSquare color={theme.colors.blue} />}
                                            className="btn btn-icon" 
                                            onClick={() => handleDeleteRow(rowIndex)} // Altere isso para editar, se necessário
                                        />
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </TableStyle>
                </>
            ):(
                <Box> Not found items here... </Box>
            )}



            <Footer>
                <p>{tableData.length} registros</p>
                <Paginator
                    currentPage={currentPage}
                    totalPages={totalPages}
                    onPageChange={handlePageChange}
                />
            </Footer>
        </div>
    );
};

export default Table;