import { useForm } from "react-hook-form";
import { ContainerForm } from "./styles";
import Input from "../../Input";
import { Button } from "../../Button";
import { useTheme } from "../../../contexts/ThemeContext";
import { FieldProps } from "../../../types/interfaces";

interface FormProps {
    fields: FieldProps[];
    onSubmit: (data: any) => void;
    columns?: number;
    method?: string;
}

const Form = ({ fields, columns = 3, onSubmit, method = "POST" }: FormProps) => {
    const { theme } = useTheme();
    const { register, handleSubmit, watch } = useForm();

    return (
        <ContainerForm theme={theme} columns={columns}>
            <form onSubmit={handleSubmit(onSubmit)} method={method}>
                {fields.map((field) => (
                    <div className="form-group" key={field.name}>
                        <label>{field.label}</label>
                        <Input
                            {...register(field.name, { required: field.required })}
                            type={field.type}
                            placeholder={field.placeholder}
                            disabled={field.disabled}
                        />
                    </div>
                ))}
                <Button className="btn btn-primary" type="submit" name="Save" />
            </form>
        </ContainerForm>
    );
};

export default Form;
