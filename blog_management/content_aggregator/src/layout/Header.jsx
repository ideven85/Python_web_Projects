//import React from 'react';
/*
Dark variants for components were deprecated in Bootstrap v5.3.0 with the introduction of color modes. Instead of adding variant="dark", set data-bs-theme="dark" on the Navbar.
 */
import {Button, Container, Form, Nav, Navbar} from "react-bootstrap";

const Header = (props) => {
    return (
        <>
            <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary  justify-content-around" >
                <Container>
                    <Navbar.Brand href="/">Content Aggregator</Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">

                    <Nav className="me-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="/about">About</Nav.Link>
                        <Nav.Link href="/basic" >Basic Form Example</Nav.Link>
                    </Nav>
                       {/* <Nav>
                            <Nav.Link href="#deets">More deets</Nav.Link>
                            <Nav.Link eventKey={2} href="#memes">
                                Dank memes
                            </Nav.Link>
                        </Nav>*/}
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
};

export default Header;