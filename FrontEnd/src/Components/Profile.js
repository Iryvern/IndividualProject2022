import React, { Component } from "react";

class Profile extends Component {
    state = { username: ""};
    
    render() 
    {
        return(
            <main className="Profile">
				<h1>Not Logged In</h1>
            </main>
        );
    }
}

export default Profile;
