<template>
  <v-card :color="workout.color" dark @click.stop="viewWorkout">
    <v-list-item two-line>
      <v-list-item-content>
        <v-list-item-title class="headline">
          <span :class="relativeDarkness">#{{ workout.id }}</span>
        </v-list-item-title>
        <v-list-item-subtitle> started {{ started }} </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-card-text>
      <v-layout row wrap align-center>
        <v-flex xs12 title text-center>
          <span :class="relativeDarkness">{{ workout.exerciseCount }}</span>
          exercises,

          <span :class="relativeDarkness">{{ workout.totalWeight || 0 }}</span>
          total weight
        </v-flex>
      </v-layout>
    </v-card-text>

    <div class="status">
      <v-chip label v-bind="{ [`color`]: `${workout.color} darken-2` }">
        <v-icon left>{{ statusIcon }}</v-icon>
        {{ getHumanStatus }}
      </v-chip>
    </div>

    <v-divider light />

    <v-card-actions>
      <v-toolbar dense flat dark :color="workout.color">
        <v-btn small icon @click.stop="archiveWorkout">
          <v-icon>archive</v-icon>
        </v-btn>

        <v-spacer />

        <v-btn small icon @click.stop="shareWorkout">
          <v-icon>share</v-icon>
        </v-btn>

        <v-btn small icon @click.stop="favoriteWorkout">
          <v-icon>favorite</v-icon>
        </v-btn>
      </v-toolbar>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mutations } from "@/graphql";
import {
  STATUS_MAP,
  PENDING,
  COMPLETE,
  IN_PROGRESS,
  CANCELLED
} from "@/constants";

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
      return distanceInWords(new Date(), data.workout.startedAt, {
        addSuffix: true
      });
    },

    ended: data => {
      if (data.workout.endedAt) {
        return format(data.workout.endedAt, "YYYY-MM-DD [@] h:MMA");
      }

      return "∞";
    },

    statusIcon: data => {
      return {
        [PENDING]: "hourglass_empty",
        [IN_PROGRESS]: "hourglass_full",
        [CANCELLED]: "cancel",
        [COMPLETE]: "check_circle"
      }[data.workout.status];
    },

    relativeDarkness: data => {
      const { color } = data.workout;

      const textColor = `${color}--text`;
      const textColorDarkened = "text--darken-4";

      return {
        [textColor]: true,
        [textColorDarkened]: true
      };
    }
  },

  methods: {
    favoriteWorkout() {
      return;
    },
    shareWorkout() {
      return;
    },
    archiveWorkout() {
      const workoutId = this.$props.workout.id;

      this.$apollo.mutate({
        mutation: mutations.RemoveWorkout,

        variables: {
          workoutId
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
      const { workout } = this.$props;

      if (workout.status === PENDING) {
        return this.$router.push(`/workouts/${workout.id}/setup`);
      }

      return this.$router.push(`/workouts/${workout.id}`);
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
