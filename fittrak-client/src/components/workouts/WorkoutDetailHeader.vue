<template>
<v-flex xs12>
  <v-layout justify-space-between>
    <v-flex xs2 text-xs-left>
      <Back />
    </v-flex>

    <v-flex xs2 text-xs-right>
      <StartWorkout v-if="pending" />
    </v-flex>
    <v-flex xs2 text-xs-right v-if="!complete && inProgress">
      <FinishWorkout />
    </v-flex>
      <!--
      <p class="control">
        <ReopenWorkout :workout=workout v-if="complete" />
      </p>
      -->
  </v-layout>
</v-flex>
</template>

<script>
import StartWorkout from "@/components/workouts/StartWorkout";
import FinishWorkout from "@/components/workouts/FinishWorkout";
import Back from "@/components/app/Back";

import { COMPLETE, PENDING, IN_PROGRESS } from "@/constants";

export default {
  name: "WorkoutDetailHeader",

  components: {
    StartWorkout,
    FinishWorkout,
    Back
  },

  computed: {
    complete() {
      const { status } = this.$props;

      return Boolean(status && status === COMPLETE);
    },
    pending() {
      const { status } = this.$props;

      return Boolean(status && status === PENDING);
    },
    inProgress() {
      const { status } = this.$props;

      return Boolean(status && status === IN_PROGRESS);
    }
  },

  props: {
    status: String
  }
};
</script>
