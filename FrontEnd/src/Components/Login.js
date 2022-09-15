import React, { Component } from "react";
import axios from "axios";

class Login extends Component {
	state = { 
		username: "",
		password: "",};

	handleLogIn = async () => {
		const headers = {"Content-type":"application/json"}
		const res = await axios.post('http://127.0.0.1:5000/login', { username: this.state.username , password: this.state.password},{headers:headers});
		console.log(res.data["access_token"])
		sessionStorage.setItem("token",res.data["access_token"])
		window.location.reload(false)
	};
	
	handleUserInput  = (e) => {
		const name = e.target.name;
		const value = e.target.value;
		this.setState({[name]: value});
		}

	render()  {
		return (
			<main className="LogIn">
				<h1>Log In</h1>
				<p className="Input">
					<input  className="Username"
						type="text"
						placeholder="Username"
						required
						name="username"
						value={this.state.username}
						onChange={this.handleUserInput}
					></input>
				</p>
				<p className="Input">
					<input className="Password"
						type="password"
						placeholder="Password"
						required
						name="password"
						value={this.state.password}
						onChange={this.handleUserInput}
					></input>
				</p>
				<p>
					<button onClick={this.handleLogIn}>Log In</button>
				</p>
			</main>
		);
	}
}

export default Login;
