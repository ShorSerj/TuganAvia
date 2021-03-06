import React, { Component } from "react";
import './sass/app.scss';

class App extends Component {
  state = {
    counter: 0
  };
  handleClick = () => {
    this.setState(prevState => {
      return { counter: prevState.counter + 1 };
    });
  };
  render() {
    return (
      <div className="App">
        <h1>I`&apos;`m configuring setting up Webpack!!!</h1>
        <p>{`The count now is: ${this.state.counter}`}</p>
        <button onClick={this.handleClick}>Click me</button>
      </div>
    );
  }
}
export default App;