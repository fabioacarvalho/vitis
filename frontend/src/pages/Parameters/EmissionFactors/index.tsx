import { FaSeedling} from "react-icons/fa6";
import { Container } from "../../../components/Container";
import Table from "../../../components/Table";
import { useState } from "react";


const EmissionFactors = () => {
    const [emissions, setEmissions] = useState<any>([]);
    const columns = []

    return (
        <Container>
            <h1>Emission Factors <FaSeedling /></h1>
            <p>Setup here your emission factores by year.</p>
            <Table data={emissions} columns={columns}></Table>
        </Container>
    );
};

export default EmissionFactors;