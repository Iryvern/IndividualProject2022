import React, { Component } from "react";
import axios from "axios";

const token = sessionStorage.getItem("token");
const name = sessionStorage.getItem("username");
const headers= {"Content-type":"application/json","Authorization":"Bearer "+token}

class Profile extends Component {
    state = { username: "",email:"",opassword:"",password:"",rpassword:""};

    handleUserInput  = (e) => {
		const name = e.target.name;
		const value = e.target.value;
		this.setState({[name]: value});
		}

    handleChangeUsername =  async () => {
		const result = await axios.post('http://127.0.0.1:5000/change/username', { ousername: name, username: this.state.username},{headers:headers});
		console.log(result)
    }

    handleChangeEmail =  async () => {
		const result = await axios.post('http://127.0.0.1:5000/change/email', { username: this.state.username , email: this.state.email},{headers:headers});
		console.log(result)
    }

    handleChangePassword =  async () => {
        if(this.state.password === this.state.rpassword){
			const result = await axios.post('http://127.0.0.1:5000/change/password', { username: this.state.username , password: this.state.password, opassword: this.state.opassword},{headers:headers});
		    console.log(result)
		}
		else{
			console.log("Passwords don't match")
		}
    }

    render() 
    {
        return(
            <main className="Profile">
                <h1>Profile</h1>
                <p className="Input">
					<input  className="Username"
						type="text"
						placeholder="Username"
						name="username"
						value={this.state.username}
						onChange={this.handleUserInput}
					></input>
				</p>
                <p>
					<button onClick={this.handleChangeUsername}>Change Username</button>
				</p>
                <p className="Input">
					<input  className="Email"
						type="text"
						placeholder="Email"
						name="email"
						value={this.state.email}
						onChange={this.handleUserInput}
					></input>
				</p>
                <p>
					<button onClick={this.handleChangeEmail}>Change Email</button>
				</p>
                <p className="Input">
					<input  className="OPassword"
						type="text"
						placeholder="Old Password"
						name="opassword"
						value={this.state.opassword}
						onChange={this.handleUserInput}
					></input>
				</p>
                <p className="Input">
					<input  className="Password"
						type="text"
						placeholder="New Password"
						name="password"
						value={this.state.password}
						onChange={this.handleUserInput}
					></input>
				</p>
                <p className="Input">
					<input  className="RPassword"
						type="text"
						placeholder="Repeat New Password"
						name="rpassword"
						value={this.state.rpassword}
						onChange={this.handleUserInput}
					></input>
				</p>
                <p>
					<button onClick={this.handleChangePassword}>Change Password</button>
				</p>
                
            </main>
        );
    }
}

export default Profile;
