<template>
  <li>
    <div>
      ID:
      <router-link :to="{name: 'WorkoutDetail', params: { workoutId: workout.id }}">
        {{ workout.id }}
      </router-link>
    </div>

    <div>
    Started: {{ workout.dateStarted }}
    </div>

    <div v-if="workout.date_ended">Ended: {{ workout.dateEnded }}</div>

    <div>
    Status: {{ getHumanStatus }}
    </div>
    <div>Exercises: {{ exercises.length }}</div>

    <br />

    <div>
      <button class="button is-small is-outlined" v-on:click="removeWorkout">Remove</button>
    </div>
  </li>
</template>

<script>
import { STATUS_MAP } from "@/constants";
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
