import React from "react";

import { withStyles } from "@material-ui/core/styles";

import Grid from "@material-ui/core/Grid";
import grey from "@material-ui/core/colors/grey";

const styles = theme => {
  return {
    root: {
      flexGrow: 1,
      backgroundColor: grey[200]
    },
    item: {
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column"
    }
  };
};

const MainLayout = props => {
  const { classes } = props;

  return (
    <Grid container className={classes.root}>
      <Grid item xs={12} className={classes.item}>
        {props.children}
      </Grid>
    </Grid>
  );
};

export default withStyles(styles)(MainLayout);
