import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import './Navigationbar.css';

const token = localStorage.getItem("token") ;
const isLoggedIn = (token && token !== "" && token !== undefined)? true:false

class Navigationbar extends Component{
  
  handleLogOut  = () => {
		localStorage.removeItem("token")
        window.location("/");
        window.location.reload(false)
		}


  render(){
     return (
			<div className="navigation">
        <Link className='link' to="/">Home</Link>
				<Link className='link' to="/ar">AR</Link>
        <Link className='link' to="/communities">Communities</Link>
        {(isLoggedIn === true)? "":
				[<Link key="1" className='link' to="/login">Login</Link>,
        <Link key="2" className='link' to="/register">Register</Link>]
        }
        {(isLoggedIn === false)? "":
        [<Link className='link' key="1" to="/profile">Profile</Link>,
        <Link className='link' key="2" onClick={this.handleLogOut} to="/">Log Out</Link>]
        }
			</div>
		);
}
}

export default Navigationbar;