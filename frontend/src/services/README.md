# Utilização

## ServiceMapper

Utilize o `serviceMapper.ts` para mapear os seus services para adicionar dados, ele serve para que a página `ChangeForm` gerada dinamicamente possa carregar automaticamente os services com base no identificador passado no componente `Table`, por exemplo:

> Apenas services com os métodos http `POST` e `PUT` devem ser carregados.



<br>

```typescript
    const generateState = () => {
        const modalInfos = [
            { label:  "Name", name: "name", type: "text", required: true },
            { label:  "cnpj", name: "cnpj", type: "text", required: true },
            { label:  "phone", name: "phone", type: "text", required: true },
            { label:  "email", name: "email", type: "email", required: true },
            { label:  "country", name: "country", type: "text", required: true },
            { label:  "state", name: "state", type: "text", required: true },
            { label:  "city", name: "city", type: "text", required: true },
        ]
        return {
            title: "Add Company",
            columns: 3,
            fields: modalInfos,
            postFunction: companyService.createCompany,
        }
    }

    return (
        <Container>
            <h1>Companys <FaBuilding /></h1>
            <p>Setup here your companys.</p>
            <Table
                data={companys} columns={columns}
                state={generateState()}
            ></Table>
        </Container>
    );
```

<br>

Basicamente ele é composto pelo (identificador_pai + service) por exemplo `company` e `user`:

<br>

```typescript
const serviceMapper = {
    company: {
        createCompany: companyService.createCompany,
        updateCompany: companyService.updateCompany,
    },
    user: {
        createUser: userService.createUser,
        updateUser: userService.updateUser,
    },
    // Adicione outros serviços aqui
};
```