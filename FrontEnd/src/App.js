import React, { Component } from 'react';
import Login from "./Components/Login.js";
import Register from "./Components/Register.js";
import Profile from "./Components/Profile.js";

import './App.css';

class App extends Component {
	state = {
	};

	render() {
		return (
		<React.Fragment>
		<main>
			<Profile/>
			<Login />
			<Register />
		</main>
		</React.Fragment>
		);
	}
}

export default App;