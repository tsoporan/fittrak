<template>
  <v-flex xs12>
    <v-layout justify-space-between row wrap>
      <BackButton />
      <WorkoutStartButton v-if="!complete && !inProgress" :workout="workout" />
      <WorkoutFinishButton v-if="!complete && inProgress" :workout="workout" />
    </v-layout>
  </v-flex>
</template>

<script>
import BackButton from "@/components/app/BackButton";
import WorkoutStartButton from "@/components/workouts/WorkoutStartButton";
import WorkoutFinishButton from "@/components/workouts/WorkoutFinishButton";

import { COMPLETE, PENDING, IN_PROGRESS } from "@/constants";

export default {
  name: "WorkoutDetailHeader",

  components: {
    BackButton,
    WorkoutStartButton,
    WorkoutFinishButton
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
    workout: {
      type: Object,
      required: true
    }
  }
};
</script>
