import { ContainerDiv } from "./styles";
import { Header } from "../Header";
import { Content } from "../Content";
import { Sidebar } from "../Sidebar";

export const Container = (props) => {
    return (
        <ContainerDiv>
            <Header />
            <div className="content">
                <Sidebar />
                <Content>
                    {props.children}
                </Content>
            </div>
        </ContainerDiv>
    );
}