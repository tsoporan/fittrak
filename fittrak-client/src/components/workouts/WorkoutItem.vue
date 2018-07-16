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
import { STATUS_MAP } from "@/components/constants";
import REMOVE_WORKOUT from "@/graphql/mutations/removeWorkout.graphql";

export default {
  name: "WorkoutItem",

  computed: {
    // Human friendly status
    getHumanStatus: data => {
      return STATUS_MAP[data.workout.status];
    },

    exercises: data => {
      return data.workout.exercises.filter(e => e.isActive);
    }
  },

  methods: {
    removeWorkout() {
      const workoutId = this.$props.workout.id;

      this.$apollo.mutate({
        mutation: REMOVE_WORKOUT,
        variables: {
          workoutId: workoutId
        }
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
