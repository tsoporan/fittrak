import React from "react";

import { withStyles } from "@material-ui/core/styles";

import Grid from "@material-ui/core/Grid";

const styles = theme => {
  return {
    root: {
      flex: 1
    }
  };
};

const $ContentWrapper = props => {
  const { classes } = props;

  return (
    <Grid className={classes.root} item>
      Body item
    </Grid>
  );
};

const ContentWrapper = withStyles(styles)($ContentWrapper);

export { ContentWrapper };
