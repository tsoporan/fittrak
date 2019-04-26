import React from "react";
import BottomNavigation from "@material-ui/core/BottomNavigation";
import BottomNavigationAction from "@material-ui/core/BottomNavigationAction";

import { withStyles } from "@material-ui/core/styles";

const styles = {
  root: {}
};

const AppBottomNavigation = props => {
  const { classes } = props;

  return (
    <BottomNavigation classes={classes.root} showLabels>
      <BottomNavigationAction label="New" />
      <BottomNavigationAction label="Test" />
      <BottomNavigationAction label="Test2" />
    </BottomNavigation>
  );
};

export default withStyles(styles)(AppBottomNavigation);
