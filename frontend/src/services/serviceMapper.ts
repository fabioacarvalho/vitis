import companyService from "./companyService"
import userService from "./userService";
// Importe outros serviços conforme necessário

// Mapeamento de todas as funções
const serviceMapper = {
    company: {
        createCompany: companyService.createCompany,
        updateCompany: companyService.updateCompany,
        deleteCompany: companyService.deleteCompany,
    },
    user: {
        createUser: userService.createUser,
        updateUser: userService.updateUser,
        deleteUser: userService.deleteUser,
    },
    // Adicione outros serviços aqui
};

export default serviceMapper;