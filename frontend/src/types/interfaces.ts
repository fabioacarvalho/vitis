
export interface FieldProps {
    label: string;
    name: string;
    type: string;
    required: boolean;
    placeholder?: string;
    onChange?: () => any;
    disabled?: boolean;
}


export interface NavigateChangeFormProps {
    title: string;
    fields: FieldProps[];
    columns: number;
    postFunction: () => void;
    service?: string, // based on serviceMapper.ts
    postFunctionIdentifier?: string;  // based on serviceMapper.ts
}