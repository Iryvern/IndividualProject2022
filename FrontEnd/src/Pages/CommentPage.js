import React, { Component } from 'react';
import Navigationbar from "../Components/Navigationbar.js";
import Comments from "../Components/Comments";

class CommunityAllPage extends Component{
    render(){
        return(
            <React.Fragment>
            <main>
            <Navigationbar/>
            <Comments>
                
            </Comments>
            </main>
            </React.Fragment>
        )
    }
}
export default CommunityAllPage;