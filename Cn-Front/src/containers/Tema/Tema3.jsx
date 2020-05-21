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
      respMatr: null,
      respP1: null,
      respP2: null,
      loading: true,
    };
  }

 
  submit = async () => {
    console.log(JSON.stringify({
      "a": this.state.matr1,
      "b": this.state.matr2,
    }))

    var response = await fetch("http://localhost:5000/Tema3", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        A_init: this.state.matr1,
        b_init: this.state.matr2,
      }),
    });
    console.log(response);
    this.setState({ respMatr: response });
  };

  render() {
    return (
      <div style={{ marginLeft: "15px" }}>
       
        <div>
          <p>
            P3: Înmulțirea matricelor booleene (Algoritmul celor patru ruşi) -
            Aho, A. V., Hopcroft, J. E., Ullman, J. D. (1976), The Design and
            Analysis of Computer Algorithms, Addison-Wesley.
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
          {/* <table
            style={{ border: "1px solid black", width: "25%", margin: "auto" }}
          >
            Result:
            {this.state.respMatr !== null
              ? this.state.respMatr.map((item) => {
                return <tr>{item}</tr>;
              })
              : null}
          </table> */}
        </div>
      </div>
    );
  }
}

export default Tema3;
