<template>
  <li v-if="workout.isActive">
    <div>
      ID:
      <router-link :to="{name: 'WorkoutDetail', params: { workoutId: workout.id }}">
        {{ workout.id }}
      </router-link>
    </div>
    Started: {{ workout.dateStarted }}
    Ended: {{ workout.dateEnded }}
    <div>
    Status: {{ getHumanStatus }}
    </div>
    <div>Exercises: {{ exercises.length }}</div>

    <div>
    <button v-on:click="removeWorkout">Remove</button>
    </div>
  </li>
</template>

<script>
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
  },

  props: {
    workout: Object
  }
};
</script>

<style scoped>
li {
  padding: 10px;
}
</style>
