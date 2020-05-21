import React, { Component } from "react";
import { Header, Icon, Image, Menu, Segment, Sidebar } from "semantic-ui-react";
import { Route, Switch, Link } from "react-router-dom";
import PowerSettingsNewIcon from "@material-ui/icons/PowerSettingsNew";
import PeopleIcon from "@material-ui/icons/People";
import Tema1 from "../Tema/Tema1";
import ErrorPage from "../ErrorPage/Error";
import "../../global/global.css";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import * as actionTypes from "../../store/actions/actions";
import Tema2 from "../Tema/Tema2";
import Tema3 from "../Tema/Tema3";

class CMS extends Component {
  render() {
    return (
      <div className="page">
        <Sidebar
          as={Menu}
          inverted
          visible
          vertical
          width="thin"
          icon="labeled"
        >
          <Link to="/tema1">
            <Menu.Item name="users">Tema1</Menu.Item>
          </Link>
          <Link to="/tema2">
            <Menu.Item name="users">Tema2</Menu.Item>
          </Link>
          <Link to="/tema3">
            <Menu.Item name="users">Tema3</Menu.Item>
          </Link>
          <Link to="/tema4">
            <Menu.Item name="users">Tema4</Menu.Item>
          </Link>

          <Link to="/tema6">
            <Menu.Item name="users">Tema6</Menu.Item>
          </Link>
          <Link to="/tema7">
            <Menu.Item name="users">Tema7</Menu.Item>
          </Link>
        </Sidebar>
        <Switch>
          <Route path="/tema1" component={Tema1} />
          <Route path="/tema2" component={Tema2} />
          <Route path="/tema3" component={Tema3} />
          <Route path="/tema4" component={Tema1} />
          <Route path="/tema6" component={Tema1} />
          <Route path="/tema7" component={Tema1} />
        </Switch>
      </div>
    );
  }
}
const mapStateToProps = (state) => {
  return {
    isLogin: state.isLogin,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    Logout: () => {
      dispatch({
        type: actionTypes.LOG_OUT,
      });
    },
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(CMS);
