<template>
  <v-list-tile @click.stop="viewWorkout">

    <v-list-tile-content>
      <v-list-tile-title>
        {{ $props.workout.id }}. Workout started <span>{{ started }}</span>
      </v-list-tile-title>
      <v-list-tile-sub-title>
        ID: #{{ $props.workout.slug}},
        Status: {{ getHumanStatus}}
        <div v-if="workout.date_ended">, Ended: {{ ended }}</div>
      </v-list-tile-sub-title>
    </v-list-tile-content>

    <v-list-tile-action>
      <v-btn icon @click.stop="removeWorkout">
        <v-icon>delete</v-icon>
      </v-btn>
    </v-list-tile-action>

  </v-list-tile>
</template>

<script>
import { STATUS_MAP } from "@/constants";
import REMOVE_WORKOUT from "@/graphql/mutations/removeWorkout.graphql";
import WORKOUTS from "@/graphql/queries/workouts.graphql";

import { format } from "date-fns";
import distanceInWords from "date-fns/distance_in_words";

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
      return distanceInWords(new Date(), data.workout.dateStarted, {
        addSuffix: true
      });
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
        },

        update(store) {
          const data = store.readQuery({ query: WORKOUTS });

          console.log("data --", data);
        }
      });
    },

    viewWorkout() {
      const workoutId = this.$props.workout.id;

      this.$router.push(`/workouts/${workoutId}`);
    }
  },

  props: {
    workout: Object
  }
};
</script>

<style scoped>
</style>
