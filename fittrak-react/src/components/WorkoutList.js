import React from "react";

import { Query } from "react-apollo";

import WorkoutCard from "./WorkoutCard";
import queries from "../graphql/queries";

class WorkoutList extends React.Component {
  render() {
    return (
      <Query query={queries.workoutsQuery}>
        {({ loading, error, data }) => {
          if (loading) return "Loading workouts ...";
          if (error) return "Error loading workouts";

          return data.workouts.map(workout => {
            return <WorkoutCard key={workout.id} workout={workout} />;
          });
        }}
      </Query>
    );
  }
}

export default WorkoutList;
