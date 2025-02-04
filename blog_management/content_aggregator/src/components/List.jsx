//import React from 'react';

import Items from "./Items.jsx";
import {Col, Row} from "react-bootstrap";

const List = ({list,onRemoveItem}) => {
    //const {list} = props;

          const sortedList = list.sort((s1,s2) =>s1.created_at_i<s2.created_at_i)
    return (
        <>
              <Row md={2} xs={1} lg={3} className="g-3">
                {sortedList.map((item) => (
                    <Col key={item.objectID}>

                        <Items item={item} onRemoveItem={onRemoveItem}/>
                    </Col>

                ))}
            </Row>

        </>
    );
};

export default List;