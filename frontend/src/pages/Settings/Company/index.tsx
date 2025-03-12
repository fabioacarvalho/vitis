import { FaBuilding} from "react-icons/fa6";
import { Container } from "../../../components/Container";
import Table from "../../../components/Table";
import { useEffect, useState } from "react";
import companyService from "../../../services/companyService";


const Company = () => {
    const [companys, setCompanys] = useState<any>([]);
    const columns = ["id", "name", "cnpj", "phone", "email", "active", "country",]


    const fetchCompanys = async () => {
        const response = await companyService.getCompanys();
        console.log(response)
        if (response.status !== 200){
            throw new Error("Failed to fetch companys");
        } else {
            const data = response.data.map((company) => (
                {...company}
            ));
            setCompanys(data);
        }
    };

    const generateState = () => {
        const fields = [
            { label:  "Name", name: "name", type: "text", required: true },
            { label:  "cnpj", name: "cnpj", type: "text", required: true },
            { label:  "phone", name: "phone", type: "text", required: true },
            { label:  "email", name: "email", type: "email", required: true },
            { label:  "cep", name: "cep", type: "text", required: true },
            { label:  "code", name: "code", type: "text", required: false },
            { label:  "country", name: "country", type: "text", required: true },
            { label:  "state", name: "state", type: "text", required: true },
            { label:  "city", name: "city", type: "text", required: true },
            { label:  "active", name: "active", type: "checkbox", required: false, placeholder: "Ativo por padrão." },
            { label:  "address", name: "address", type: "text", required: true },
            { label:  "message", name: "message", type: "text", required: false },
        ]
        return {
            title: "Add Company",
            columns: 3,
            fields: fields,
            service: "company",
            postFunctionIdentifier: "createCompany",
        }
    }

    useEffect(() => {
        fetchCompanys();
    }, []);

    return (
        <Container>
            <h1>Companys <FaBuilding /></h1>
            <p>Setup here your companys.</p>
            <Table
                data={companys} columns={columns}
                formState={generateState()}
            ></Table>
        </Container>
    );
};

export default Company;