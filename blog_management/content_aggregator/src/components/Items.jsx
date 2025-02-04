//import React from 'react';
import {Button, Card} from "react-bootstrap";
import ListGroup from "react-bootstrap/ListGroup";

/**
 * Use <Card.Body> to pad content inside a <Card>.
 * Using <Card.Title>, <Card.Subtitle>, and <Card.Text> inside the <Card.Body> will line them up nicely. <Card.Link>s are used to line up links next to each other.
 *
 * <Card.Text> outputs <p> tags around the content, so you can use multiple <Card.Text>s to create separate paragraphs.
 *
 */
const dateFormatter = (item) => {
    //console.log(typeof(item));
    const temp = item.split("-");
   // console.log(temp);
    
    //const date_created = new Date(item);
    //console.log(date_created);
    
    //const date =    date_created.getDay() +"/"+date_created.getMonth() + "/" + date_created.getFullYear();
    const date = temp[1]+"/"+temp[2].substring(0,2)+"/"+temp[0];
    return date;
}

const Items = ({item,onRemoveItem}) => {
    //const {item}=props;
   /* const handleRemoveItem = () => {
        onRemoveItem(item);
    };*/
      return (

       <>
            <Card style={{ width: '18rem' }} className="h-100">
                <Card.Body className="d-flex flex-column">


                    <Card.Title className="d-flex justify-content-between align-items-baseline mb-4"><Card.Link href={item.url} style={{ textDecoration: "none",color: "brown"}} target="_blank">{item.title}</Card.Link></Card.Title>

                    <Card.Subtitle>Written by: {item.author}</Card.Subtitle>
                    <Card.Text>

                        Comments: {item.num_comments} &nbsp;

                    </Card.Text>
                    <Card.Text> Created at: {dateFormatter(item.created_at)}</Card.Text>
                    <Card.Text>

                        Points: {item.points} &nbsp;

                    </Card.Text>
                    <Card.Text> Updated at: {dateFormatter(item.updated_at)}</Card.Text>



                </Card.Body>

                <Button type="button" onClick={() =>onRemoveItem(item)}>Remove</Button>

            </Card>

        </>

    );
};

export default Items;