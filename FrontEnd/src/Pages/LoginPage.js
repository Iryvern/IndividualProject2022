import React, { Component } from 'react';
import Login from "../Components/Login";
import Navigationbar from "../Components/Navigationbar.js";

class LoginPage extends Component{
    render(){
        return(
            <React.Fragment>
            <main>
            <Navigationbar/>
            <Login>
            </Login>
            </main>
            </React.Fragment>
        )
    }
}
export default LoginPage;