<template>
  <div>
    <button class="button is-primary is-outlined" v-on:click="createWorkout">Create New Workout</button>
  </div>
</template>

<script>
import WORKOUTS from "@/graphql/queries/workouts.graphql";
import CREATE_WORKOUT from "@/graphql/mutations/createWorkout.graphql";

import { PENDING } from "@/constants";

export default {
  name: "CreateWorkout",

  methods: {
    createWorkout() {
      this.$apollo
        .mutate({
          mutation: CREATE_WORKOUT,

          update: (store, { data }) => {
            const newWorkout = data.createWorkout.workout;
            const result = store.readQuery({
              query: WORKOUTS,
              variables: { status: PENDING }
            });

            // Prepend the latest workout
            result.workouts.unshift(newWorkout);

            store.writeQuery({
              query: WORKOUTS,
              variables: { status: PENDING },
              data: result
            });
          }
        })
        .then(resp => {
          const workout = resp.data.createWorkout.workout;

          this.$router.push({
            name: "WorkoutDetail",
            params: { workoutId: workout.id }
          });
        });
    }
  }
};
</script>
