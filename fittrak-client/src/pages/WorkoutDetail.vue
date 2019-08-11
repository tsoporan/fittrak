<template>
  <div style="height:100%">
    <AppBar :title="title" />
    <v-container fill-height fluid v-if="$apollo.loading">
      <v-layout
        fill-height
        row
        align-center
        justify-center
        justify-content-center
      >
        <v-flex text-center>
          <Loader size="64" color="primary" />
          <p text-xs-center class="headline">
            🏋️ Loading workout ...
          </p>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container v-else fluid>
      <v-layout v-if="exercises.length" row pa-3 mb-12>
        <v-flex mb-3>
          <Tip>
            <template v-slot:icon>
              🏋️
            </template>
            You're on your way to a stronger you 💪! Mark an exercise and
            workout <v-icon color="green">check_circle</v-icon> when you're done
            with them! You can also <v-icon color="blue">pause</v-icon> your
            workout and get back to it later or
            <v-icon color="orange">settings</v-icon> to configure your
            exercises. Enjoy! 💚
          </Tip>
        </v-flex>
        <ExerciseList :exercises="exercises" />
      </v-layout>
      <v-layout v-else fill-height row align-center justify-center>
        <p text-xs-center class="headline">
          Hrm, no exercises? 🤔
        </p>
      </v-layout>
      <WorkoutFooter>
        <v-btn color="darkGrey" @click.stop="goBack" icon>
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-btn color="orange" @click.stop="workoutSetup" icon>
          <v-icon>settings</v-icon>
        </v-btn>

        <v-btn color="blue" @click.stop="pauseWorkout" icon>
          <v-icon>pause</v-icon>
        </v-btn>

        <v-btn
          :loading="loading"
          color="green"
          @click.stop="finishWorkout"
          icon
        >
          <v-icon>check_circle</v-icon>
        </v-btn>
      </WorkoutFooter>
    </v-container>
  </div>
</template>

<script>
import { queries } from "@/graphql";
import { mutations } from "@/graphql";

import { COMPLETE } from "@/constants";
import { showSnackbar } from "@/helpers";

import Loader from "@/components/app/Loader";
import ExerciseList from "@/components/exercises/ExerciseList";
import AppBar from "@/components/app/AppBar";
import Tip from "@/components/app/Tip";
import WorkoutFooter from "@/components/workouts/WorkoutFooter";

export default {
  name: "Workout",

  data() {
    return {
      workout: {},
      exercises: [],
      title: `Workout #${this.$route.params.workoutId}`,
      loading: false
    };
  },

  apollo: {
    workout: {
      query: queries.workoutQuery,
      variables() {
        const workoutId = this.$route.params.workoutId;

        return {
          workoutId
        };
      },
      update: data => data.workout
    },

    exercises: {
      query: queries.exercisesQuery,
      variables() {
        const workoutId = this.$route.params.workoutId;

        return {
          workoutId
        };
      },
      update: data => data.exercises
    }
  },

  methods: {
    goBack() {
      return this.$router.go(-1);
    },

    workoutSetup() {
      return this.$router.push({
        name: "WorkoutSetup",
        params: {
          workoutId: this.workout.id
        }
      });
    },

    pauseWorkout() {
      console.log("pause workout");
    },

    finishWorkout() {
      const workout = this.workout;

      if (workout.status === COMPLETE) {
        return this.$router.push({
          name: "FitTrak"
        });
      }

      this.loading = true;

      this.$apollo
        .mutate({
          mutation: mutations.updateWorkoutMutation,

          variables: {
            workoutId: workout.id,
            workoutFields: {
              endedAt: new Date(),
              status: COMPLETE
            }
          }
        })
        .then(() => {
          this.loading = false;

          this.$router.push({
            name: "FitTrak"
          });

          showSnackbar("success", "Workout finished.");
        })
        .catch(() => {
          this.loading = false;

          showSnackbar(
            "error",
            "Oops, could not finish workout. Support has been notified.",
            true
          );
        });
    }
  },

  components: {
    AppBar,
    Tip,
    ExerciseList,
    Loader,
    WorkoutFooter
  }
};
</script>
