import React, { Component} from "react";
import axios from "axios";
import './Community.css';

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const community_name = urlParams.get('c');

class Community extends Component {
	state = {posts: [],
    members:[] };

    componentDidMount() {
    this.getAllPosts();
    }
    
    getAllPosts = async () => {
		axios.get("http://127.0.0.1:8081/community", {headers: {"Content-Type": "application/json"},params: {community: community_name}})
			.then((res) => {
				this.setState({ posts: res.data.posts });
                this.setState({ members: res.data.members});
			});
	};

    handleJoin = async (community_name) => {
		
	};

	render()  {
		return (
			<div className = "top">
                    <h1>{community_name}</h1>
                    <p>
                            <button onClick={() => this.handleJoin(community_name)}>Join</button>
                    </p>
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
                                    <button onClick={() => this.handleLike()}>Like</button>
                                    <button onClick={() => this.handleComment()}>Comment</button>
                                </p>
                            </div>
                        ))}
			</div>
			</div>
		);
	}
}

export default Community;
