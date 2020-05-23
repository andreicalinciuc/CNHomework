import React, { Component } from "react";
import "./Users.css";
import { Input, Button } from "@material-ui/core";
class Tema1 extends Component {
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

  componentDidMount = async () => {
    var responseP1 = await fetch(
      "http://localhost:5000/Tema1/p1"
    ).then((response) => response.json());
    var responseP2 = await fetch(
      "http://localhost:5000/Tema1/p2"
    ).then((response) => response.json());
    console.log(responseP1);
    console.log(responseP2);
    this.setState({ respP1: responseP1, respP2: responseP2, loading: false });
  };
  submit = async () => {
    var response = await fetch("http://localhost:5000/Tema1/p3", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        mat1: this.state.matr1,
        mat2: this.state.matr2,
      }),
    }).then((response) => response.json());

    console.log(response);
    this.setState({ respMatr: response });
  };

  render() {
    return (
      <div style={{ marginLeft: "15px" }}>
        <div>
          <p>
            P1: Să se găsească cel mai mic număr pozitiv <b>u > 0</b>, de forma{" "}
            <b>u = 10-m</b>
            care satisface proprietatea: <b>1 1 + ≠ c u</b> unde prin +c am
            notat operația de adunare efectuată de calculator. Numărul u se
            numește precizia mașină.
          </p>
          <b>
            {this.state.loading === false
              ? ` Result: ${this.state.respP1.result}`
              : "wait.."}
          </b>
        </div>
        <div>
          <p>
            P2: Operația +c este <b>neasociativă</b>: fie numerele{" "}
            <b>x=1.0 , y = u , z = u</b>, unde u este precizia mașină calculată
            anterior. Să se verifice că operația de adunare efectuată de
            calculator este neasociativă: ( ) () cc cc xy zx yz + + ≠+ + . Să se
            găsească un exemplu pentru care operația de înmulțire ×c este
            neasociativă.
          </p>
          <b>
            {this.state.loading === false
              ? ` Result:[${this.state.respP2.result}]`
              : "wait.."}
          </b>
        </div>
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
          <table
            style={{ border: "1px solid black", width: "25%", margin: "auto" }}
          >
            Result:
            {this.state.respMatr !== null
              ? this.state.respMatr.map((item) => {
                return <tr>{item}</tr>;
              })
              : null}
          </table>
        </div>
      </div>
    );
  }
}

export default Tema1;
