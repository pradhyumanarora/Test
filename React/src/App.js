import './App.css';
import { Link } from "react-router-dom";

// import Navbar from "./components/Navbar/Navbar";
// import {WebcamCapture} from "./components/Webcam/Webcam";
// import MusicPlayer from "./components/Music-Player/MusicPlayer";
import Index from './components/Login';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import Homepage from  './components/Homepage'

function App() {
  return (
      <>
    {/* <Index/> */}
    
    <Index path="/homepage" render={Homepage} />
    {/* <Navbar/>
    <WebcamCapture/>
        <MusicPlayer/> */}
        {/* <GetExpression/> */}
      </>
  );
}

export default App;
