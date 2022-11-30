import React, { Component } from 'react';
import Navigationbar from "../Components/Navigationbar.js";
import Community from "../Components/Community";

class CommunityAllPage extends Component{
    render(){
        return(
            <React.Fragment>
            <main>
            <Navigationbar/>
            <Community>
                
            </Community>
            </main>
            </React.Fragment>
        )
    }
}
export default CommunityAllPage;