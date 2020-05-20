import React, { Component } from "react";

class ErrorPage extends Component {
  render() {
    return (
      <div
        style={{
          width: "100%",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
        }}
      >
        <h1>404</h1>
        <h4>Uh oh! Are you sure you wanted to go here?</h4>
      </div>
    );
  }
}
export default ErrorPage;
