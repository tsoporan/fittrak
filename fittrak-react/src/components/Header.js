import React from "react";

import { withStyles } from "@material-ui/core/styles";

import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";

const styles = {
  root: {
    flexGrow: 1
  }
};

const $AppHeader = props => {
  const { classes, pageTitle } = props;

  return (
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6" color="inherit">
            {pageTitle}
          </Typography>
        </Toolbar>
      </AppBar>
  );
};

const AppHeader = withStyles(styles)($AppHeader);

export { AppHeader };
