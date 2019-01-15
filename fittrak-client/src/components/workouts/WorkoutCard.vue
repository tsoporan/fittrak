<template>
  <v-card
    :color="workout.color"
    dark
    @click.stop="viewWorkout"
  >
    <v-card-title primary-title> 
      <span class="headline">Workout from {{ started }}</span>

      <div v-if="workout.date_ended">, Ended: {{ ended }}</div>

    </v-card-title>

    <v-card-text>
      <div>
        Time Spent:
      </div>
      <div>
        Total Weight:
      </div>
    </v-card-text>

    <div class="status">
      <v-chip 
        label 
        v-bind="{[`color`]: `${workout.color} darken-2`}"
      >
        <v-icon left>label</v-icon>
        {{ getHumanStatus }}
      </v-chip>
    </div>

    <v-divider light />

    <v-card-actions>
      <v-toolbar 
        flat 
        dark 
        :color="workout.color">

        <v-btn 
          icon>
          <v-icon>share</v-icon>
        </v-btn>

        <v-spacer />

        <v-btn 
          icon>
          <v-icon>favorite</v-icon>
        </v-btn>
        <v-btn 
          @click.stop="removeWorkout"
          icon>
          <v-icon>delete</v-icon>
        </v-btn>
      </v-toolbar>
    </v-card-actions>

  </v-card>
</template>

<script>
import { queries, mutations } from "@/graphql";
import { STATUS_MAP } from "@/constants";

import { format } from "date-fns";
import distanceInWords from "date-fns/distance_in_words";

export default {
  name: "WorkoutCard",

  computed: {
    // Human friendly status
    getHumanStatus: data => {
      return STATUS_MAP[data.workout.status];
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
        mutation: mutations.RemoveWorkout,

        variables: {
          workoutId: workoutId
        }

        /*
        update(store) {
          const data = store.readQuery({
            query: query.WorkoutsQuery
          });

          const filteredWorkouts = data.workouts.filter(
            wrk => wrk.id !== workoutId
          );

          data.workouts = filteredWorkouts;

          store.writeQuery({
            query: query.WorkoutsQuery,
            data
          });
        }
        */
      });
    },

    viewWorkout() {
      const workoutId = this.$props.workout.id;

      this.$router.push(`/workouts/${workoutId}`);
    }
  },

  props: {
    workout: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
div.status {
  position: absolute;
  right: -10px;
  top: -11px;
}
</style>
