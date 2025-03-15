import { useForm } from "react-hook-form";
import ChangeFormDefault from "../../../../components/ChangeFormDefault";
import { Container } from "../../../../components/Container";
import { Button } from "../../../../components/Button";
import Input from "../../../../components/Input";
import companyService from "../../../../services/companyService";

const CompanyChangeForm = () => {
    const { register, handleSubmit, formState } = useForm();
    const onSubmit = data => console.log(data);

    const fields = [
        { label: "Name", name: "name", type: "text", required: true },
        { label: "CNPJ", name: "cnpj", type: "text", required: true },
        { label: "Phone", name: "phone", type: "text", required: true },
        { label: "Email", name: "email", type: "email", required: true },
        { label: "CEP", name: "cep", type: "text", required: true },
        { label: "Code", name: "code", type: "text", required: false },
        { label: "Country", name: "country", type: "text", required: true },
        { label: "State", name: "state", type: "text", required: true },
        { label: "City", name: "city", type: "text", required: true },
        { label: "Active", name: "active", type: "checkbox", required: false, placeholder: "Ativo por padrão." },
        { label: "Address", name: "address", type: "text", required: true },
        { label: "Message", name: "message", type: "text", required: false },
    ];

    // const onSubmit = async (data: any) => {
    //     console.log('Form Data:', data); // Verifique os dados antes de enviar
    //     try {
    //         const response = await companyService.createCompany(data);
    //         console.log("Success:", response);
    //     } catch (error) {
    //         console.error("Error:", error);
    //     }
    //     alert("Ok"); // Alerta para confirmar que o onSubmit foi chamado
    // };

    return (
        <Container>
            <ChangeFormDefault handleSubmit={handleSubmit} columns={3}>
                {fields.map((field) => (
                    <div className="form-group" key={field.name}>
                        <label>{field.label}</label>
                        <Input
                            type={field.type}
                            {...register(field.name, { required: field.required })}
                            placeholder={field.placeholder}
                            disabled={field.disabled}
                        />
                    </div>
                ))}
            </ChangeFormDefault>
            {/* <form onSubmit={handleSubmit(onSubmit)}>
                <input type="submit" />
                <Button className="btn btn-primary" type="submit" name="Save" />
            </form> */}
        </Container>
    );
};

export default CompanyChangeForm;