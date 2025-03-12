import { Container } from "../../components/Container";
import { StepsGuide, Step, Callout, SimpleTable, Header, Body } from "../../components/StepsGuide";
import { FaFlagCheckered } from "react-icons/fa6";

const Help = () => {
    return (
        <Container>
            <h1>Start here <FaFlagCheckered /></h1>
            <StepsGuide>
                <Step number={1} title="Step number 1">
                    <h2>Go to somewhere...</h2>
                    <img src="./imgx.png" alt="step-guide" />
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                </Step>
                <Step number={2} title="Step number 2">
                    <h2>Doing this</h2>
                    <ul>
                        <li>Lorem ipsum dolor sit amet.</li>
                        <li>Lorem ipsum dolor sit amet.</li>
                        <li>Lorem ipsum dolor sit amet.</li>
                    </ul>
                    <Callout>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Suscipit nobis provident ad.
                    </Callout>
                    <SimpleTable>
                        <Header>
                            <tr>
                                <th>Value 1</th>
                                <th>Value 2</th>
                            </tr>
                        </Header>
                        <Body>
                            <tr>
                                <td>Data 1</td>
                                <td>Data 2</td>
                            </tr>
                        </Body>
                    </SimpleTable>
                </Step>

                <Step number={3} title="Import data" >
                    <p>So if you want import some data, you can follow this steps.</p>

                    <h3>Download template</h3>
                    <p>First thing you need to do is, download the template, so follow the under steps:</p>
                    <ul>
                        <li>Into your page you'll can see a button called "Import Data";</li>
                        <li>Click it and it'll open a modal;</li>
                        <li>In this modal you'll looking for another button called "Download Tamplete";</li>
                        <li>Click there and get your template;</li>
                        <li>After took your template, filling data following the patters into template;</li>
                    </ul>

                    <h3>Import template</h3>
                    <p>After download and filled templete, you need import, so you can do this:</p>
                    <ul>
                        <li>Into the same screen you'll can see another space called, drag your file xlsx;</li>
                        <li>You can drag your file into there or click in the box and attched the file.</li>
                        <li>After that, the system will process the file automatically, so now just wait end the process.</li>
                    </ul>
                </Step>
            </StepsGuide>
        </Container>
    );
};

export default Help;