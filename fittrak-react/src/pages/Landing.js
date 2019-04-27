import React from "react";

import { withStyles } from "@material-ui/core/styles";

import Fab from "@material-ui/core/Fab";
import AddIcon from "@material-ui/icons/Add";

import MainLayout from "../layouts/Main";
import AppHeader from "../components/Header";
import { AppBottomNavigation } from "../components/Navigation";
import { ContentWrapper } from "../components/Content";

const styles = theme => {
  console.log("theme", theme);
  return {
    fab: {
      position: "absolute",
      bottom: theme.spacing.unit * 4.5,
      left: "50%",
      transform: "translateX(-50%)"
    }
  };
};

const Landing = props => {
  const { viewer, classes } = props;

  return (
    <MainLayout>
      <AppHeader pageTitle="FitTrak" viewer={viewer} />
      <ContentWrapper>
        <p>
          Welcome {viewer.username}({viewer.email})
        </p>
      </ContentWrapper>

      <Fab
        size="small"
        className={classes.fab}
        color="secondary"
        aria-label="Create Workout"
      >
        <AddIcon />
      </Fab>
      <AppBottomNavigation />
    </MainLayout>
  );
};

export default withStyles(styles)(Landing);
