<template>
  <v-list-tile @click.stop="viewWorkout">
    <v-list-tile-content>
      <v-list-tile-title>#{{ $props.workout.id}}</v-list-tile-title>
      <v-list-tile-sub-title>
        Started: {{ started }}
      </v-list-tile-sub-title>

      <v-list-tile-sub-title>
        <div v-if="workout.date_ended">Ended: {{ ended }}</div>
      </v-list-tile-sub-title>

      <v-chip label color="secondary" text-color="white">{{ getHumanStatus }}</v-chip>

    </v-list-tile-content>

    <v-list-tile-action>
      <v-btn icon @click.stop="removeWorkout">
        <v-icon color="error">delete</v-icon>
      </v-btn>
    </v-list-tile-action>

  </v-list-tile>
</template>

<script>
import { STATUS_MAP } from "@/constants";
import REMOVE_WORKOUT from "@/graphql/mutations/removeWorkout.graphql";

import { format } from "date-fns";

export default {
  name: "WorkoutItem",

  computed: {
    // Human friendly status
    getHumanStatus: data => {
      return STATUS_MAP[data.workout.status];
    },

    exercises: data => {
      return data.workout.exercises.filter(e => e.isActive);
    },

    started: data => {
      return format(data.workout.dateStarted, "YYYY-MM-DD [@] h:MMA");
    },

    ended: data => {
      return format(data.workout.dateEnded, "YYYY-MM-DD [@] h:MMA");
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
    },

    viewWorkout() {
      const workoutId = this.$props.workout.id;

      this.$history.push(`/workouts/${workoutId}`);
    }
  },

  props: {
    workout: Object
  }
};
</script>

<style scoped>
</style>
