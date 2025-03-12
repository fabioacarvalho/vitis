import { ContainerForm } from "./styles";
import Input from "../Input/index";
import { useTheme } from "../../../contexts/ThemeContext";
import { FieldProps } from "../../types/interfaces";
interface FormProps {
    fields: FieldProps[];
    columns?: number;
    method?: string;
    action?: string;
}

const Form = ({ fields, columns, method, action }: FormProps) => {
    const { theme } = useTheme();

    return (
        <ContainerForm theme={theme} columns={columns}>
            {fields.map((field) => (
                <div className="form-group" key={field.name}>
                    <label>
                        {field.label}
                    </label>
                    <Input
                        type={field.type}
                        name={field.name}
                        onChange={field?.onChange}
                        required={field.required}
                        placeholder={field?.placeholder}
                        disabled={field?.disabled}
                    />
                </div>
            ))}
        </ContainerForm>
    );
};

export default Form;