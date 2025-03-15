import { Container } from "../../components/Container";
import { CRadarChart } from "../../components/Charts/CRadarChart";
import { CLineChart } from "../../components/Charts/CLineChart";
import { CBarChart } from "../../components/Charts/CBarChart";
import { CAreaChart } from "../../components/Charts/CAreaChart";

const Dashboard = () => {
    return (
        <Container>
            <h1>Dashboard</h1>

            <CLineChart />
            <CAreaChart />
            <CRadarChart />
            <CBarChart />


        </Container>
    );
};

export default Dashboard;