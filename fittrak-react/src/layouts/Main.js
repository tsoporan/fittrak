import React from "react";

import { withStyles } from "@material-ui/core/styles";

import Grid from "@material-ui/core/Grid";

const styles = theme => {
  return {
    root: {
      flexGrow: 1
    }
  };
};

const MainLayout = props => {
  const { classes } = props;

  return (
    <div className={classes.root}>
      <Grid>{props.children}</Grid>
    </div>
  );
};

export default withStyles(styles)(MainLayout);
