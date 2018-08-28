<template>
   <v-btn color="info" depressed @click.stop="finishWorkout">Finish Workout</v-btn>
</template>

<script>
import UPDATE_WORKOUT from "@/graphql/mutations/updateWorkout.graphql";
import { COMPLETE } from "@/constants";

export default {
  name: "FinishWorkout",
  methods: {
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

  props: {
    workout: Object
  }
};
</script>
