<template>
<v-flex xs12>
  <v-layout justify-space-between row wrap>
    <v-flex>
      <Back />
    </v-flex>

    <v-flex v-if="!complete && !inProgress" text-xs-right>
      <v-btn color="success" depressed @click.stop="startWorkout">Start</v-btn>
    </v-flex>

    <v-flex v-if="!complete && inProgress" text-xs-right>
      <v-btn color="info" depressed @click.stop="finishWorkout">Finish</v-btn>
    </v-flex>

    <!--
    <v-flex xs2 text-xs-right v-if="complete">
      <v-btn color="info" depressed @click.stop="finishWorkout">Finish Workout</v-btn>
    </v-flex>
    -->
  </v-layout>
</v-flex>
</template>

<script>
import UPDATE_WORKOUT from "@/graphql/mutations/updateWorkout.graphql";

import Back from "@/components/app/Back";

import { COMPLETE, PENDING, IN_PROGRESS } from "@/constants";

export default {
  name: "WorkoutDetailHeader",

  components: {
    Back
  },

  methods: {
    startWorkout() {
      const { workout } = this.$props;

      this.$apollo.mutate({
        mutation: UPDATE_WORKOUT,

        variables: {
          workoutId: workout.id,
          workoutFields: {
            dateStarted: new Date(),
            status: IN_PROGRESS
          }
        }
      });
    },

    finishWorkout() {
      const { workout } = this.$props;

      this.$apollo
        .mutate({
          mutation: UPDATE_WORKOUT,

          variables: {
            workoutId: workout.id,
            workoutFields: {
              dateEnded: new Date(),
              status: COMPLETE
            }
          }
        })
        .then(() => {
          this.$router.push({
            name: "Home"
          });
        });
    }
  },

  computed: {
    complete() {
      const { status } = this.$props.workout;

      return Boolean(status && status === COMPLETE);
    },
    pending() {
      const { status } = this.$props.workout;

      return Boolean(status && status === PENDING);
    },
    inProgress() {
      const { status } = this.$props.workout;

      return Boolean(status && status === IN_PROGRESS);
    }
  },

  props: {
    workout: Object
  }
};
</script>
