import React from "react";

import { withStyles } from "@material-ui/core/styles";

import BottomNavigation from "@material-ui/core/BottomNavigation";
import BottomNavigationAction from "@material-ui/core/BottomNavigationAction";

import ShowChart from "@material-ui/icons/ShowChart";
import History from "@material-ui/icons/History";
import Settings from "@material-ui/icons/Settings";
import List from "@material-ui/icons/List";

const styles = {
  root: {}
};

class $LandingNavigation extends React.Component {
  state = {
    value: 0
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };

  render() {
    const { classes } = this.props;
    const { value } = this.state;

    return (
      <BottomNavigation
        className={classes.root}
        showLabels
        value={value}
        onChange={this.handleChange}
      >
        <BottomNavigationAction label="Workouts" icon={<List />} />
        <BottomNavigationAction label="Progress" icon={<ShowChart />} />
        <BottomNavigationAction label="History" icon={<History />} />
        <BottomNavigationAction label="Settings" icon={<Settings />} />
      </BottomNavigation>
    );
  }
}

const LandingNavigation = withStyles(styles)($LandingNavigation);

export { LandingNavigation };
