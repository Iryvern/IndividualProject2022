import React, { Component } from 'react';
import Login from "./Login.js";
import Register from "./Register.js";

import './App.css';

class App extends Component {
	state = {
	};

	render() {
		return (
		<React.Fragment>
		<main>
			<Login />
			<Register />
		</main>
		</React.Fragment>
		);
	}
}

export default App;