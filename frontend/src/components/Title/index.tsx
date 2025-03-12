import { useTheme } from "../../contexts/ThemeContext";
import { TitleContainer } from "./styles"

interface TitleProps {
    name: string;
    others?: any[];
};

const Title = ({ name, others }: TitleProps) => {
    const { theme } = useTheme()
    return <TitleContainer theme={theme} {...others}>{name}</TitleContainer>
};
export default Title;