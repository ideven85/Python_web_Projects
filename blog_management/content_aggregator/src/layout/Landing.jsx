/*import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'*/
import {Accordion, Button, Card, Container} from "react-bootstrap";
import * as React from "react";
import useStorageState from "../hooks/useLocalStorage.js";
import axios from "axios";
import List from "../components/List.jsx";
import BasicExample from "../components/BasicExample.jsx";
import Header from "./Header.jsx";
import Search from "../components/Search.jsx";

/*
const initial_stories = [
    {
        objectId: 0,
        title: "React",
        url: 'https://reactjs.org/',
        author: 'Jordan Walke',
        num_comments: 3,
        points: 4,

    },
    {
        objectId: 1,
        title: "Learn Python",
        url: 'https://python.org/',
        author: 'deven kalra',
        num_comments: 3000,
        points: 400,
    },
    {
        objectId: 2,
        title: "Java Github Repository",
        url: 'https://github.com/ideven85/Java_Coding_Interview',
        author: 'Deven Kalrea',
        num_comments: 300000,
        points: 4000,
    },
    {
        objectId: 3,
        title: "Python Repository",
        url: 'https://github.com/ideven85/Machine_Learning_Algorithms',
        author: 'Deven Kalra',
        num_comments: 30000,
        points: 40,
    }
];
*/
/*   React.useEffect(() => {
       dispatchStories({ type: 'STORIES_FETCH_INIT' });
       getAsyncStories()
           .then((result) => {
               dispatchStories({
                   type: 'STORIES_FETCH_SUCCESS',
                   payload: result.data.stories,
               });
           })
           .catch(() =>
               dispatchStories({ type: 'STORIES_FETCH_FAILURE' })
           );
   }, []);*/
/*const loadingFunction = () => {
    console.log("Still loading");
    return(
       <p>Loading</p>
    )
}*/
/*const getAsyncStories = () => new Promise((resolve) =>
    setTimeout(
            () =>  resolve({data: {stories: initial_stories}}),
        2000)
);*/
const API_ENDPOINT = 'https://hn.algolia.com/api/v1/search?query=';

const Landing = () => {
    //const [count, setCount] = useState(0);


    //const [stories, setStories] = React.useState([]);
    /*   const [isLoading, setIsLoading] = React.useState(false);
       const [isError,setIsError] = React.useState(false);
    */
    const storiesReducer = (state, action) => {
        switch (action.type) {
            case 'STORIES_FETCH_INIT':
                return {
                    ...state,
                    isLoading: true,
                    isError: false,
                };
            case 'STORIES_FETCH_SUCCESS':
                return {
                    ...state,
                    isLoading: false,
                    isError: false,
                    data: action.payload,
                };
            case 'STORIES_FETCH_FAILURE':
                return {
                    ...state,
                    isLoading: false,
                    isError: true,
                };
            case 'REMOVE_STORY':
                return {
                    ...state,
                    data: state.data.filter(
                        (story) => action.payload.objectID !== story.objectID
                    ),
                };
            default:
                throw new Error();
        }
    };

    const [stories, dispatchStories] = React.useReducer(storiesReducer,
        {data: [], isLoading: false, isError: false});


    const [searchTerm, setSearchTerm] = useStorageState('search', 'React');
    const [url, setUrl] = React.useState(
        `${API_ENDPOINT}${searchTerm}`
    );

    //New Feature

    /*
        const handleFetchStories = React.useCallback(() => { // B

            dispatchStories({ type: 'STORIES_FETCH_INIT' });
            fetch(url)
                .then((response) => response.json())
                .then((result) => {
                    dispatchStories({
                        type: 'STORIES_FETCH_SUCCESS',
                        payload: result.hits,
                    });
                })
                .catch(() =>
                    dispatchStories({ type: 'STORIES_FETCH_FAILURE' })
                );
        }, [url]); // E
    */

    const handleFetchStories = React.useCallback(async () => {
        dispatchStories({type: 'STORIES_FETCH_INIT'});
        try {
            const result = await axios.get(url);

            dispatchStories({
                type: 'STORIES_FETCH_SUCCESS',
                payload: result.data.hits,
            });

        }catch{
            dispatchStories({
                type: 'STORIES_FETCH_FAILURE'
            })
        }

    },[url])

    React.useEffect(() => {
        handleFetchStories(); // C
    }, [handleFetchStories]); // D
    /*const handleRemoveStory = (item) => {
        const new_stories = stories.data.filter(s=>s.objectId !== item.objectId);
      //  setStories(new_stories); Removed from state to reducer..
       // const new_stories = stories.filter((story) => item.objectId !==story.objectId);
        dispatchStories({
            type: 'REMOVE_STORY',
            payload: new_stories
        });
    }*/
    /*const ids = [];
    for(let s of stories){
        ids.push(s.objectId);
    }*/

    //Using Hook to set search term...
    //todo Storing user preferences.. like the story's objectIds he has removed..?
    // Then not rendering those stories upon refresh...
    //Could be a big feature
    // Not a bad idea...

    const handleRemoveStory = (item) => {
        dispatchStories({
            type: 'REMOVE_STORY',
            payload: item,
        });
    };
    const handleSearch = (event) => {
        setSearchTerm(event.target.value);
        event.preventDefault();
    };
    const handleSearchSubmit = () => {
        setUrl(`${API_ENDPOINT}${searchTerm}`);
    }

    // const searchedStories = stories.filter((story) =>
    /* const searchedStories = stories.data.filter((story) => story.length>0
         && story.title.toLowerCase().includes(searchTerm.toLowerCase() || story.author.toLowerCase().includes(searchTerm.toLowerCase()))
     );*/


    /*const searchedStories = stories.data.filter((story) =>
        story.data.title.toLowerCase().includes(searchTerm.toLowerCase()) || story.data.author.toLowerCase().includes(searchTerm.toLowerCase())
    );*/
    return (
        <>





            <Container style={{margin: "100px"}}>
                {/*    <p>Number of matching titles: {titles.length}</p>
                    <p>Number of matching authors: {authors.length}</p>
*/}
                {stories.isError && <b>Something went wrong...</b>}



                    <Search search={searchTerm} onSearch={handleSearch}> Search: </Search> &nbsp;&nbsp;

                <br />
                {stories.isLoading ?
                    (<div style={{margin: "100px"}}><p>Loading</p></div>)
                    : (
                        <List list={stories.data} onRemoveItem={handleRemoveStory}/>
                    )
                }
            </Container>






        </>
    )
}

export default Landing;
