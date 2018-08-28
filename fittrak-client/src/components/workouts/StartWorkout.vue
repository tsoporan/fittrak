<template>
  <v-btn color="success" depressed @click.stop="startWorkout">Start</v-btn>
</template>

<script>
import UPDATE_WORKOUT from "@/graphql/mutations/updateWorkout.graphql";
import { IN_PROGRESS } from "@/constants";

export default {
  name: "StartWorkout",
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
    }
  },

  props: {
    workout: Object
  }
};
</script>
