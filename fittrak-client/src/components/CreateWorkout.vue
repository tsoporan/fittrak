<template>
  <div>
    <button v-on:click="createWorkout">Create New Workout</button>
  </div>
</template>

<script>
import VIEWER_WORKOUTS from "@/graphql/queries/viewerWorkouts.graphql";
import CREATE_WORKOUT from "@/graphql/mutations/createWorkout.graphql";

export default {
  name: "CreateWorkout",

  methods: {
    createWorkout() {
      this.$apollo.mutate({
        mutation: CREATE_WORKOUT,

        update: (store, { data }) => {
          const newWorkout = data.createWorkout.workout;
          const res = store.readQuery({ query: VIEWER_WORKOUTS });

          res.viewer.workouts.push(newWorkout);

          store.writeQuery({ query: VIEWER_WORKOUTS, data: res });
        },

        optimisticResponse: {
          __typename: "Mutation",
          createWorkout: {
            __typename: "createWorkout",
            workout: {
              __typename: "WorkoutType",
              id: -1,
              isActive: true,
              status: "IN_PROGRESS",
              exercises: [],
              dateStarted: null,
              dateEnded: null,
              slug: null
            }
          }
        }
      }).then(resp => {
        const workout = resp.data.createWorkout.workout;

        this.$router.push({ name: "WorkoutDetail", params: { workoutId: workout.id }});
      }).catch(err => {
        console.error(err);
      });

    }
  }
};
</script>
