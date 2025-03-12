import { Container } from "../../components/Container";
import Table from "../../components/Table";
import Title from "../../components/Title/index";
import Form from "../../components/Form";

const Items = () => {
    const columns = ["Name", "Age", "Country"];
    const data = [
      { Name: "John", Age: 30, Country: "USA" },
      { Name: "Jane", Age: 25, Country: "Canada" },
      { Name: "Max", Age: 35, Country: "Germany" },
    ];
  
    return (
        <Container>
            <Title name="Items"/>
            <Table columns={columns} data={data} />
        </Container>
    )
};

export default Items;