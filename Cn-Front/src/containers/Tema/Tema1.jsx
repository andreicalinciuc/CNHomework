import React, { Component } from "react";
import users from "../../global/usersList";
import "./Users.css";
import { Input } from "@material-ui/core";
class Tema1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      matr1: null,
      matr2: null,
    };
  }

  render() {
    return (
      <div>
        <div>
          <p>Ex 1</p>
          <p>cel mai mic nr..: </p>
        </div>
        <div>
          <p>Ex 2</p>
          <p>cel mai mic nr..: </p>
        </div>
        <div>
          <p>Ex 3</p>
          <div>
            <p>Matr1:</p>
            <Input
            multiline={true}
            rowsMax={15}
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
              onChange={(e) => {
                this.setState({
                  matr2: e.target.value,
                });
              }}
            />
          </div>
        </div>
        <p>{this.state.matr1}</p>
        <p>{this.state.matr2}</p>
      </div>
    );
  }
}

export default Tema1;
