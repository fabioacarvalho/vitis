import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom"; // Importando useNavigate
import { AuthContext } from "../../contexts/AuthContext";
import { FaUser, FaLock } from "react-icons/fa";
import {
    SignUpContainer,
    SignUpBox,
    Title,
    InputGroup,
    Input,
    Icon,
    CheckboxContainer,
    SignUpButton,
    LinksContainer
} from "./styles";

const SignUp: React.FC = () => {
    const auth = useContext(AuthContext);
    const navigate = useNavigate(); // Inicializando o hook de navegação
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [email, setEmail] = useState("");

    const handleSignUp = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!username || !password || !email || !confirmPassword) {
            alert("Please fill in all fields");
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }

        if (auth) {
            try {
                // Chamar a API de signup, passando os dados do usuário
                const response = await fetch("http://127.0.0.1:8000/signup/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ username, email, password }),
                });

                if (!response.ok) {
                    throw new Error("Failed to sign up");
                }

                // Se o signup for bem-sucedido, redireciona para o login
                navigate("/sign-in");
            } catch (error) {
                console.error(error);
                alert("Sign up failed: " + error.message);
            }
        }
    };

    return (
        <SignUpContainer>
            <SignUpBox>
                <Title>Sign Up</Title>
                <form onSubmit={handleSignUp}>
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
                            <FaUser />
                        </Icon>
                        <Input
                            type="email"
                            placeholder="Email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
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
                    <InputGroup>
                        <Icon>
                            <FaLock />
                        </Icon>
                        <Input
                            type="password"
                            placeholder="Confirm Password"
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                        />
                    </InputGroup>
                    <CheckboxContainer>
                        <input type="checkbox" id="agree" />
                        <label htmlFor="agree">I agree to the terms and conditions</label>
                    </CheckboxContainer>
                    <SignUpButton type="submit">SIGN UP</SignUpButton>
                </form>
                <LinksContainer>
                    <span>Already have an account? <a href="/sign-in">Login</a></span>
                </LinksContainer>
            </SignUpBox>
        </SignUpContainer>
    );
};

export default SignUp;