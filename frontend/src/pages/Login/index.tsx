import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom"; // Importando useNavigate
import { AuthContext } from "../../contexts/AuthContext";
import { FaUser, FaLock } from "react-icons/fa";
import {
    LoginContainer,
    LoginBox,
    Title,
    InputGroup,
    Input,
    Icon,
    CheckboxContainer,
    LoginButton,
    LinksContainer
} from "./styles";

const Login: React.FC = () => {
    const auth = useContext(AuthContext);
    const navigate = useNavigate(); // Inicializando o hook de navegação
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
    
        if (!username || !password) {
            alert("Please enter both username and password");
            return;
        }
    
        if (auth) {
            const success = await auth.login(username, password);
            if (success) {
                navigate("/"); // Redireciona para a rota inicial
            }
        }
    };

    const handleLogin2 = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!username || !password) {
            alert("Please enter both username and password");
            return;
        }

        if (auth) {
            const response = await auth.login(username, password); // Passando navigate para o login
            if (response) {
                navigate("/"); // Redireciona para a rota inicial
            }
        }
    };

    return (
        <LoginContainer>
            <LoginBox>
                <Title>Login</Title>
                <form onSubmit={handleLogin}>
                    <InputGroup>
                        <Icon>
                            <FaUser />
                        </Icon>
                        <Input
                            type="text"
                            placeholder="Username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </InputGroup>
                    <InputGroup>
                        <Icon>
                            <FaLock />
                        </Icon>
                        <Input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </InputGroup>
                    <CheckboxContainer>
                        <input type="checkbox" id="remember" />
                        <label htmlFor="remember">Remember me</label>
                    </CheckboxContainer>
                    <LoginButton type="submit">LOGIN</LoginButton>
                </form>
                <LinksContainer>
                    <a href="#">Forgot your password?</a>
                    <span>New here? <a href="/sign-up">Sign Up</a></span>
                </LinksContainer>
            </LoginBox>
        </LoginContainer>
    );
};

export default Login;