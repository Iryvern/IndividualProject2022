import React, { Component } from "react";
import axios from "axios";

const token = sessionStorage.getItem("token") ;


class Profile extends Component {
    state = { username: ""};

    handleLogOut  = () => {
		sessionStorage.removeItem("token")
        window.location.reload(false)
		}

    handleTokenTest  = async () => {
		const headers = {"Content-type":"application/json","Authorization":"Bearer "+token}
		const res = await axios.post('http://127.0.0.1:5000/test',{headers:headers});
        console.log(res)
		}

    render() 
    {
        return(
            <main className="Profile">
                {(token && token !== "" && token !== undefined)? "You are logged in":
				<h1>Not Logged In</h1>
                }
                <button onClick={this.handleLogOut}>Log Out</button>
                <button onClick={this.handleTokenTest}>Test Token</button>
            </main>
        );
    }
}

export default Profile;
