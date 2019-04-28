import React from "react";

import { withStyles } from "@material-ui/core/styles";

import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

const styles = {};

class WorkoutCard extends React.Component {
  render() {
    const { workout } = this.props;

    return (
      <Card>
        <CardContent>
          <Typography gutterBottom>Workout {workout.id}</Typography>
          <CardActions>
            <Button size="small">Learn More</Button>
          </CardActions>
        </CardContent>
      </Card>
    );
  }
}

export default withStyles(styles)(WorkoutCard);
