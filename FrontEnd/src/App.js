import React, { Component } from 'react';
import Login from "./Components/Login.js";
import Register from "./Components/Register.js";
import LogInStatus from "./Components/LogInStatus.js";
import Profile from "./Components/Profile.js";

import './App.css';

class App extends Component {
	state = {
	};

	render() {
		return (
		<React.Fragment>
		<main>
			<LogInStatus/>
			<Login />
			<Register />
			<Profile />
		</main>
		</React.Fragment>
		);
	}
}

export default App;