import { Container } from "../../../components/Container";
import { FaInbox } from "react-icons/fa6";
import { Button } from "../../components/Button";
import Form from "../../components/Form";
import { FieldProps } from "../../types/interfaces";

interface ChangeListProps {
    title: string;
    columns: number;
    fields: FieldProps[];
    handleSave?: () => void;
}

const ChangeList = ({ title, columns, fields, handleSave }: ChangeListProps) => {

    const onSubmit = (e: React.FormEvent) => {
        e.preventDefault(); // Evita o comportamento padrão do formulário
        console.log("Form submitted");

        // Coleta os dados do formulário
        const formData = new FormData(e.target as HTMLFormElement);
        const data = Object.fromEntries(formData.entries());

        if (handleSave) {
            try {
                const response = await handleSave(data); // Passa os dados para `saveFunction`
                console.log("Save function response:", response);
            } catch (error) {
                console.error("Error in save function:", error);
            }
        } else {
            console.log("No save function provided");
        }
    };

    return (
        <Container>
            <h1>{title} <FaInbox /></h1>
            <form action="." method="POST" onSubmit={onSubmit}>
                <div>
                    <Form
                        columns={columns ? columns : 3}
                        fields={fields}
                        method="post"
                        action="/"
                    />
                </div>
                <div>
                    <Button type="submit" name="Save"/>
                    <Button type="submit">Save</Button>
                </div>
            </form>
        </Container>
    )
}

export default ChangeList;