import React, { Component } from 'react';
import Navigationbar from "../Components/Navigationbar.js";
import CommunityAll from "../Components/CommunityAll";

class CommunityAllPage extends Component{
    render(){
        return(
            <React.Fragment>
            <main>
            <Navigationbar/>
            <CommunityAll>
                
            </CommunityAll>
            </main>
            </React.Fragment>
        )
    }
}
export default CommunityAllPage;