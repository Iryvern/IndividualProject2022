import React, { Component} from "react";
import axios from "axios";
import './CommunityAll.css';

class CommunitityAll extends Component {
	state = {communties:[]};

    componentDidMount() {
    this.getAll();
    }

    getAll = async () => {
		axios
			.get(
				"http://188.166.201.183/a-communities"
			)
			.then((res) => {
				this.setState({ communties: res.data });
			});
	};

    handleView = async (community_name) => {
		window.location = "/community?c="+community_name;
	};

	render()  {
		return (
			<div className="communities">
                    {this.state.communties.map((comm) => (
					<div className="community" key={comm._id}>
						<h1>{comm.community}</h1>
                        <h2>Members: {comm.members.length}</h2>
                        <p>
                            <button onClick={() => this.handleView(comm.community)}>View</button>
                        </p>
					</div>
				))}
			</div>
		);
	}
}

export default CommunitityAll;
