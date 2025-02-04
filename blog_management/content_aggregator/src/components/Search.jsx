import React from 'react';
import {Button, Form} from "react-bootstrap";

const Search = (props) => {

    //const {search,onSearch}=props;
    console.log(props.search);
    return (
        <>
            <Form className="d-flex" onSubmit={props.handleSearchSubmit}>
                <Form.Control
                    type="search"
                    placeholder="Search"
                    className="me-2"
                    aria-label="Search"

                    value={props.search}
                    onChange={props.onSearch}
                />
                <Button variant="primary" disabled={!props.search} type="submit">Submit</Button>
            </Form>



        </>
    );
};

export default Search;