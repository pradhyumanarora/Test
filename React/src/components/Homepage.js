import Navbar from "./Navbar/Navbar";
import {WebcamCapture} from "./Webcam/Webcam";
import MusicPlayer from "./Music-Player/MusicPlayer";
import Player from "./Player";

function Homepage(){
    return(
        <>
            <Navbar/>
            <WebcamCapture/>
            <MusicPlayer/>
            {/* <Player/> */}
        </>
    );
}

export default Homepage;