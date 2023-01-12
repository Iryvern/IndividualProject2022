import React, { Component } from 'react';
import Navigationbar from "./Components/Navigationbar.js";
import Logo from "./Components/images/tempuslogo.png";

import './App.css';
//Testing
class App extends Component {
	state = {
	};

	render() {
		return (
		<React.Fragment>
		<main>
			<Navigationbar/>
			<h1 style = {{paddingLeft:"35%"}}>Welcome to TempusReality</h1>
			<img
					src={Logo}
					height="100"
					width="125"
					className="m-2"
					alt="Company Logo"
					style = {{paddingLeft:"45%"}}
			/>
		</main>
		</React.Fragment>
		);
	}
}

export default App;