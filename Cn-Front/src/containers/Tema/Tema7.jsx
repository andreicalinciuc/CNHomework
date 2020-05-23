import React, { Component } from "react";
import users from "../../global/usersList";
import "./Users.css";
import { Input, Button } from "@material-ui/core";
class Tema7 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      matr1: -1,
      matr2: null,
      respMatr: null,
      respMatr2: null,
      respP1: null,
      respP2: null,
      loading: true,
    };
  }

  submit = async () => {
    var response = await fetch("http://localhost:5000/Tema7/solve", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        test_index: parseInt(this.state.matr1),
      }),
    }).then((response) => response.json());

    this.setState({ respMatr: response });
  };

  render() {
    return (
      <div style={{ marginLeft: "15px", width: "100%" }}>
        <div>
          <p>
            Metoda Laguerre de aproximare a radacinilor reale ale unui polinom
          </p>
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "space-evenly",
            }}
          >
            <div>
              <p>test_index:</p>
              <Input
                multiline={true}
                rowsMax={10}
                onChange={(e) => {
                  this.setState({
                    matr1: e.target.value,
                  });
                }}
              />
              <p style={{ color: "red" }}>
                {this.state.matr1 < 0 || this.state.matr1 > 3
                  ? "Input between 0 and 3"
                  : null}
              </p>
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
              <p>Result:</p>
              <p>{this.state.respMatr}</p>
            </div>
          ) : null}
        </div>
      </div>
    );
  }
}

export default Tema7;
