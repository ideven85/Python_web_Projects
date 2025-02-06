import React from 'react';
import { Routes, Route } from "react-router-dom";
import About from "./layout/About.jsx";
import {Container} from "react-bootstrap";
import Landing from "./layout/Landing.jsx";
import 'bootstrap/dist/css/bootstrap.min.css';
import BasicExample from "./components/BasicExample.jsx";
import Header from "./layout/Header.jsx";
import './App.css';

const  App = () => {
    return (
        <Container>
            <Header />

            <div >
                <Routes>
                    <Route path="/" element={<Landing/>}/>
                    <Route path="/about" element={<About/>}/>
                    <Route path="/basic" element={<BasicExample/>}/>
                </Routes>
            </div>
        </Container>

                );

}
export default App;