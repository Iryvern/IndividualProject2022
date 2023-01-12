import React, { Component} from "react";
import axios from "axios";

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const post_id = urlParams.get('p');

class Comments extends Component {
	state = {post: [],
    comments:[],
    comment:"" };

        
    componentDidMount() {
    this.getPost();
    }

    handleUserInput  = (e) => {
		const name = e.target.name;
		const value = e.target.value;
		this.setState({[name]: value});
		}
    
    getPost = async () => {
		axios.get("http://188.166.201.183/p-get", {headers: {"Content-Type": "application/json"}, params: {"post_id": post_id}})
			.then((res) => {
				this.setState({ post: res.data});
                console.log(this.state.post.comments);
			});
	};

    handleLike = async (post_id) => {
	};

    handleComment = async (community_name) => {
		
	};

	render()  {
		return (
            <>
            <div className="post" key={""}>
                <h2>{this.state.post.title}</h2>
                <h2>{this.state.post.creator}</h2>
                <h2>{this.state.post.content}</h2>
                <h2>Likes: {this.state.post.likes}</h2>
                <h2>Comments: {this.state.post.n_comments}</h2>
                <h2>Date{this.state.post.date}</h2>
                <p>
                    <button onClick={() => this.handleLike("post._id")}>Like</button>
                </p>
            </div>
            <div>
            <p className="Input">
					<input className="comment"
						type="text"
						placeholder="Leave a comment..."
						name="comment"
						value={this.state.comment}
						onChange={this.handleUserInput}
					></input>
				</p>
				<p>
					<button onClick={this.handleComment}>Post Comment</button>
				</p>
            </div>
            </>
		);
	}
}

export default Comments;
