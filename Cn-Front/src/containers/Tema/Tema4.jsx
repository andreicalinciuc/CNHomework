import React, { Component } from "react";
import "./Users.css";
import { Input, Button } from "@material-ui/core";
class Tema4 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      matr1: null,
      matr2: null,
      respMatr: null,
      respP1: null,
      respP2: null,
      loading: true,
    };
  }

  submit = async () => {
    console.log(
      JSON.stringify({
        a: this.state.matr1,
        b: this.state.matr2,
      })
    );

    var response = await fetch("http://localhost:5000/Tema4/solve", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        a: this.state.matr1,
        b: this.state.matr2,
      }),
    }).then((response) => response.json());
    console.log(response);
    this.setState({ respMatr: response });
  };

  render() {
    return (
      <div style={{ marginLeft: "15px", width: "100%" }}>
        <div>
          <p>Rezolvarea unui sistem de ecuatii cu matrici rare:</p>
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "space-evenly",
            }}
          >
            <div>
              <p>Matr1:</p>
              <Input
                multiline={true}
                rowsMax={10}
                onChange={(e) => {
                  this.setState({
                    matr1: e.target.value,
                  });
                }}
              />
            </div>
            <div>
              <p>Matr2:</p>
              <Input
                multiline={true}
                rowsMax={10}
                onChange={(e) => {
                  this.setState({
                    matr2: e.target.value,
                  });
                }}
              />
            </div>
          </div>
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            flexDirection: "column",
            margin: "10px",
          }}
        >
          <Button onClick={() => this.submit()}>Submit</Button>
          {this.state.respMatr !== null ? (
            <div>
              <p>{this.state.respMatr.result}</p>
              
            </div>
          ) : null}
        </div>
      </div>
    );
  }
}

export default Tema4;
