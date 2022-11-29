import React, { Component } from 'react';
import Register from "../Components/Register";
import Navigationbar from "../Components/Navigationbar.js";

class RegisterPage extends Component{
    render(){
        return(
            <React.Fragment>
            <main>
            <Navigationbar/>
            <Register>
            </Register>
            </main>
            </React.Fragment>
        )
    }
}
export default RegisterPage;