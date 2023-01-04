import React, { Component} from "react";
import axios from "axios";
import './Community.css';

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const community_name = urlParams.get('c');
const username = localStorage.getItem("username") ;

class Community extends Component {
	state = {posts: [],
    members:[] };

        
    componentDidMount() {
    this.getAllPosts();
    }
    
    getAllPosts = async () => {
		axios.get("http://127.0.0.1:8081/community", {headers: {"Content-Type": "application/json"}, params: {"community": community_name}})
			.then((res) => {
				this.setState({ posts: res.data.posts });
                this.setState({ members: res.data.members});
			});
	};

    handleJoin = async () => {
        axios.get("http://127.0.0.1:8081/c-join", {headers: {"Content-Type": "application/json"}, params: {"community":community_name, "username":username}})
			.then((res) => {
				window.location.reload(false);
			});
	};

    handleLeave = async () => {
     axios.get("http://127.0.0.1:8081/c-leave", {headers: {"Content-Type": "application/json"}, params: {"community":community_name, "username":username}})
			.then((res) => {
				window.location.reload(false);
			});
	};

    handleLike = async (post_id) => {
		axios.get("http://127.0.0.1:8081/p-like", {headers: {"Content-Type": "application/json"}, params: {"post_id":post_id,"community":community_name, "username":username}})
			.then((res) => {
				window.location.reload(false);
			});
	};

    handleComment = async (post_id) => {
		window.location = "/comments?p="+post_id;
	};

	render()  {
		return (
			<div className = "top">
                    <h1>{community_name}</h1>
                    <p>
                            {(this.state.members.includes(username))?(<button onClick={() => this.handleLeave(community_name)}>Leave</button>):(<button onClick={() => this.handleJoin(community_name)}>Join</button>)}
                    </p>
                    <h3>Users:</h3>
                    <div className="users">
                        <ul>
                            {this.state.members.map((member) => (
                                <li key={member}>{member}</li>
                        ))}
                        </ul>
                    </div>
                    <div className="posts">
                        {this.state.posts.map((post) => (
                            <div className="post" key={post._id}>
                                <h2>{post.title}</h2>
                                <h2>{post.creator}</h2>
                                <h2>{post.content}</h2>
                                <h2>Likes: {post.likes}</h2>
                                <h2>Comments: {post.n_comments}</h2>
                                <h2>{post.date}</h2>
                                <p>
                                    <button onClick={() => this.handleLike(post._id)}>Like</button>
                                    <button onClick={() => this.handleComment(post._id)}>Comment</button>
                                </p>
                            </div>
                        ))}
			</div>
			</div>
		);
	}
}

export default Community;
