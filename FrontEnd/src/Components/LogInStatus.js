import React, { Component } from "react";
import axios from "axios";

const token = sessionStorage.getItem("token") ;
const isLoggedIn = (token && token !== "" && token !== undefined)? true:false

class LogInStatus extends Component {
    state = { username: ""};

    handleLogOut  = () => {
		sessionStorage.removeItem("token")
        window.location.reload(false)
		}

    handleTokenTest  = async () => {
		const headers= {"Content-type":"application/json","Authorization":"Bearer "+token}
        const data = {
            name: "Test"
        };
        console.log('http://127.0.0.1:5000/test',data,{headers:headers})
		const res = await axios.post('http://127.0.0.1:5000/test',data,{headers:headers});
        console.log(res)
		}

    render() 
    {
        return(
            <main className="LogInStatus">
                {(isLoggedIn === true)? "":
				<h1>Not Logged In</h1>
                }
                {(isLoggedIn === false)? "":
				[
                <h1 key="0">Logged In</h1>,
                <button onClick={this.handleLogOut} key="1">Log Out</button>,
                <button onClick={this.handleTokenTest} key="2">Test Token</button>
                ]
                }
            </main>
        );
    }
}

export default LogInStatus;
