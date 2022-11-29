import React, { Component } from 'react';
import Profile from "../Components/Profile";
import Navigationbar from "../Components/Navigationbar.js";

class ProfilePage extends Component{
    render(){
        return(
            <React.Fragment>
            <main>
            <Navigationbar/>
            <Profile>
            </Profile>
            </main>
            </React.Fragment>
        )
    }
}
export default ProfilePage;