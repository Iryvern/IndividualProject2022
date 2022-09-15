import React, { Component } from "react";
import axios from "axios";

class Register extends Component {
	state = { 
		username: "",
		password: "",
        rpassword: ""};

	handleRegister = () =>{
		if(this.state.password === this.state.rpassword){
			this.Register()
		}
		else{
			console.log("Passwords don't match")
		}
		
	}

	Register = async () => {
		const result = await axios.post('http://127.0.0.1:5000/register', { username: this.state.username , password: this.state.password});
		console.log(result)
	};
	
	handleUserInput  = (e) => {
		const name = e.target.name;
		const value = e.target.value;
		this.setState({[name]: value});
		}

	render() {
		return (
			<main className="Register">
				<h1>Register</h1>
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
                <p className="Input">
					<input className="Password"
						type="password"
						placeholder="Repeated Password"
						required
						name="rpassword"
						value={this.state.rpassword}
						onChange={this.handleUserInput}
					></input>
				</p>
				<p>
					<button onClick={this.handleRegister}>Register</button>
				</p>
			</main>
		);
	}
}

export default Register;