import { Container } from "../../components/Container";
import Table from "../../components/Table";
import Title from "../../components/Title/index";
import userService from "../../services/userService";
import { useEffect, useState } from "react";

const Users = () => {
    const [users, setUsers] = useState([]);

    const columns = ["id", "username", "email"];

    const fetchUsers = async () => {
        try {
            const response = await userService.getUsers();
            if (response.status !== 200) {
                throw new Error("Failed to fetch users");
            } else {                
                const data = response.data.map((user: any) => ({
                    id: user.id,
                    username: user.username,
                    email: user.email,
                }));
                setUsers(data);
            }
        } catch (error) {
            console.error("Failed to fetch users:", error);
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <Container>
            <Title name="Users"/>
            <Table columns={columns} data={users} />
        </Container>
    );
};

export default Users;