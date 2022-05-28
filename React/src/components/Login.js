import React,{useState} from 'react'
import Button from '@mui/material/Button';
// import Cookies from 'js-cookie';
import {Cookie} from 'react-cookie';
// ?sessionid='+Cookies.get('sessionid')

export default function Index(){
    // const [auth, setAuth] = useState();
    const authenticateSpotify = ()=>{
        // console.log(Cookie.get('sessionid'));
        console.log(document.cookie);
        fetch('http://localhost:8000/spotify/is-authenticated')
        .then((response) => response.json())
        .then((data) => {   
            // setAuth(data.status);
            // console.log(Cookies.get('sessionid'));
            console.log(data);

            if(!(data.status)){
                fetch('http://localhost:8000/spotify/auth')
                .then((response) => response.json())
                .then((data) => {
                    window.location.replace(data.url);
                })
                // console.log('Hii');
            }
        })
    }
    return(
        <div>
            <h1>Hello</h1>
            <Button variant="contained" onClick={(e)=>{
                e.preventDefault(); 
                authenticateSpotify();
            }}>Hello World</Button>


            
        </div>
    );    
}

