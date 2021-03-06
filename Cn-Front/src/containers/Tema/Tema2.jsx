import React, { Component } from "react";
import users from "../../global/usersList";
import "./Users.css";
import { Input, Button } from "@material-ui/core";
class Tema2 extends Component {
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
        A_init: this.state.matr1,
        b_init: this.state.matr2,
      })
    );

    var response = await fetch("http://localhost:5000/Tema2", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        A_init: this.state.matr1,
        b_init: this.state.matr2,
      }),
    }).then((response) => response.json());
    console.log(response);
    this.setState({ respMatr: response });
  };

  render() {
    return (
      <div style={{ marginLeft: "15px", width: "100%" }}>
        <div>
          <p>Rezolvarea ecuatiilor liniare folosind descompunera LU:</p>
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
              <p>{this.state.respMatr.result1}</p>
              <p>{this.state.respMatr.result2}</p>
              <p>{this.state.respMatr.result3}</p>
              <p>{this.state.respMatr.result4}</p>
            </div>
          ) : null}
        </div>
      </div>
    );
  }
}

export default Tema2;
