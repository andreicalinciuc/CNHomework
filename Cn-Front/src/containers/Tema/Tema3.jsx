import React, { Component } from "react";
import users from "../../global/usersList";
import "./Users.css";
import { Input, Button } from "@material-ui/core";
class Tema3 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      matr1: null,
      matr2: null,
      matr3: null,
      matr4: null,
      respMatr: null,
      respP1: null,
      respP2: null,
      loading: false,
    };
  }

  submit = async () => {
    this.setState({ loading: true });
    var response = await fetch("http://localhost:5000/Tema3", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        a: this.state.matr1,
        b: this.state.matr2,
        aplusb: this.state.matr3,
        aorib: this.state.matr4,
      }),
    }).then((response) => response.json()); 
    console.log(response);
    this.setState({ respMatr: response, loading: false });
  };

  render() {
    return (
      <div style={{ marginLeft: "15px",width:"100%" }}>
        <div>
          <p>
          Verificare adunare si inmultire a matricilor rare:
          </p>

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
            <div>
              <p>Matr1 + Matr2:</p>
              <Input
                multiline={true}
                rowsMax={10}
                onChange={(e) => {
                  this.setState({
                    matr3: e.target.value,
                  });
                }}
              />
            </div>
            <div>
              <p>Matr1 * Matr2:</p>
              <Input
                multiline={true}
                rowsMax={10}
                onChange={(e) => {
                  this.setState({
                    matr4: e.target.value,
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
          {this.state.loading === false ? (
            this.state.respMatr !== null ? (
              <div>
                <p>{this.state.respMatr.a_plus_b}</p>
                <p>{this.state.respMatr.a_ori_b}</p>
              </div>
            ) : null
          ) : (
            "waiting result"
          )}
        </div>
      </div>
    );
  }
}

export default Tema3;
