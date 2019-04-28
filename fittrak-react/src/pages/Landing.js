import React from "react";

import { withStyles } from "@material-ui/core/styles";

import Fab from "@material-ui/core/Fab";
import AddIcon from "@material-ui/icons/Add";

import MainLayout from "../layouts/Main";
import AppHeader from "../components/Header";
import { LandingBottomNavigation } from "../components/Navigation";
import { ContentWrapper } from "../components/Content";

import WorkoutList from "../components/WorkoutList";

const styles = theme => {
  console.log("theme", theme);
  return {
    fab: {
      position: "fixed",
      bottom: theme.spacing.unit * 4.5,
      left: "50%",
      transform: "translateX(-50%)",
      zIndex: 1
    }
  };
};

class Landing extends React.Component {
  render() {
    const { classes } = this.props;

    return (
      <MainLayout>
        <AppHeader pageTitle="FitTrak" />
        <ContentWrapper>
          <WorkoutList />
        </ContentWrapper>

        <Fab
          size="small"
          className={classes.fab}
          color="secondary"
          aria-label="Create Workout"
        >
          <AddIcon />
        </Fab>
        <LandingBottomNavigation />
      </MainLayout>
    );
  }
}

export default withStyles(styles)(Landing);
