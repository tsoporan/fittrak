<template>
  <li v-if="workout.isActive">
    ID: {{ workout.id }}
    Started: {{ workout.dateStarted }}
    Ended: {{ workout.dateEnded }}
    Status: {{ getHumanStatus }}
    <h3>Exercises: {{ exercises.length }}</h3>

    <button v-on:click="removeWorkout">Remove</button>
  </li>
</template>

<script>
/*
import VIEWER_WORKOUTS from "@/graphql/queries/viewerWorkouts.graphql";
*/
import REMOVE_WORKOUT from "@/graphql/mutations/removeWorkout.graphql";

const STATUS_MAP = {
  IN_PROGRESS: "In Progress",
  CANCELLED: "Cancelled",
  COMPLETE: "Complete"
};

export default {
  name: "WorkoutItem",
  computed: {
    // Human friendly status
    getHumanStatus: data => {
      return STATUS_MAP[data.workout.status];
    },
    exercises: data => {
      return data.workout.exercises;
    }
  },
  props: {
    workout: Object
  },
  methods: {
    removeWorkout() {
      const workoutId = this.$props.workout.id;

      this.$apollo
        .mutate({
          mutation: REMOVE_WORKOUT,
          variables: {
            workoutId: workoutId
          }
        })
        .then(resp => {
          console.log("*** remove resp", resp);
        })
        .catch(err => {
          console.error("Failed to remove workout", err);
        });
    }
  }
};
</script>
