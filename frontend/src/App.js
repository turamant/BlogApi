// src/App.js
import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
    state = {
    todos: []
};

componentDidMount() {
this.getTodos();
}
// new
getTodos() {
axios
.get('http://127.0.0.1:8000/api/posts/')
.then(res => {
this.setState({ todos: res.data });
})
.catch(err => {
console.log(err);
});
}
render() {
return (
<div>
    {this.state.todos.map(item => (
        <div key={item.id}>
        <h2>{item.author}</h2>
        <h1>{item.title}</h1>
        <img src={item.foto} width={100} height={100}/>
        <span>{item.body}</span>
        <p>{item.created}</p>
        <p>{item.updated}</p>
        </div>
))}
</div>
);
}
}
export default App;