import React, { useEffect, useState, createContext } from "react";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';

const ItemsContext = createContext({
    items: [],
    fetchItems: () => {}
});

export default function Items() {
    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        const response = await fetch("http://127.0.0.1:8000/items");
        const data = await response.json();
        // FastAPI returns a direct list [...], not { data: [...] }
        setItems(Array.isArray(data) ? data : data.data || []);
    };

    // 1. Move useEffect outside fetchItems so it triggers on page load
    useEffect(() => {
        fetchItems();
    }, []);

    return (
        <ItemsContext.Provider value={{ items, fetchItems }}>
            <Container className="justify-content-xl-around mt-4">
                <Row>
                    <Col sm={8}>
                        {/* 2. Loop through items using .map() */}
                        {items.map((item) => (
                            <Card key={item.id} className="mb-3">
                                <Card.Body>
                                    <Card.Title>{item.name}</Card.Title>
                                    <Card.Text>{item.description}</Card.Text>
                                    <Card.Text>
                                        <strong>Price:</strong> ₹{item.price} |{" "}
                                        <span>{item.on_offer ? "On Offer" : "Regular Price"}</span>
                                    </Card.Text>
                                </Card.Body>
                            </Card>
                        ))}
                    </Col>
                </Row>
                <p>Go back to doing research idiot</p>
            </Container>
        </ItemsContext.Provider>
    );
}
