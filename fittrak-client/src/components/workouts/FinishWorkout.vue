<template>
  <div>
    <form>
      <button v-on:click.prevent="finishWorkout">Finish Workout</button>
    </form>
  </div>
</template>

<script>
import UPDATE_WORKOUT from "@/graphql/mutations/updateWorkout.graphql";
import { COMPLETE } from "@/components/constants";

export default {
  name: "FinishWorkout",
  methods: {
    finishWorkout() {
      const { workout } = this.$props;

      this.$apollo.mutate({
        mutation: UPDATE_WORKOUT,

        variables: {
          workoutId: workout.id,
          workoutFields: {
            dateEnded: new Date(),
            status: COMPLETE
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
