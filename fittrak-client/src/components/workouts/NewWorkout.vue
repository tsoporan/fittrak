<template>
  <v-flex text-xs-right>
    <v-dialog 
      v-model="dialog" 
      fullscreen 
      hide-overlay 
      transition="dialog-bottom-transition">
      <v-btn 
        icon
        dark
        slot="activator" 
        color="primaryDark" 
        @click.stop="dialog = true" 
        :loading="loading" 
      ><v-icon>add</v-icon></v-btn>
      <v-card>
        <v-toolbar 
          dark 
          color="primary"
          fixed
        >
          <v-btn 
            icon 
            dark 
            @click.native="dialog = false">
            <v-icon>close</v-icon>
          </v-btn>
          <v-toolbar-title>New Workout</v-toolbar-title>
          <v-spacer/>
          <v-toolbar-items>
            <v-btn 
              dark 
              flat 
              @click.native="createWorkout">Start</v-btn>
          </v-toolbar-items>
        </v-toolbar>

        <!-- Body -->

        <v-layout 
          row 
          wrap
          class="mt-4" 
        >

          <v-flex>
            <p class="headline grey--text text--darken-2 ma-3 mt-5">
              Set up your workout
            </p>
            <p class="subheading ma-3 grey--text text--darken-2">Stage your workout below by selecting exercises. Once
            you're ready hit "Start" to begin the workout.</p>
            <v-divider />
          </v-flex>

          <v-flex 
            xs12 
          >
            <v-subheader>Staged workout</v-subheader>
            <v-flex 
              v-if="selectedExercises.length" 
              mb-4
              mr-2
              ml-2
            >
              <v-chip 
                color="primaryDark"
                :key="exercise.id"
                dark
                v-for="exercise in selectedExercises"
              >
                {{ exercise.name }}
                <v-icon 
                  right
                  @click.stop="deselectExercise(exercise.id)">cancel</v-icon>
              </v-chip>
            </v-flex>
            <v-flex 
              v-else
              text-xs-center
            >
              <p class="grey--text text--darken-4">No exercises selected yet!</p>
            </v-flex>

            <v-divider/>
          </v-flex>

          <v-flex 
            xs12 
            mt-3>
            <v-subheader>Popular exercises</v-subheader>
            <v-flex 
              v-if="popularExercises.length" 
              mr-2 
              ml-2>
              <v-chip 
                v-for="exercise in popularExercises" 
                :key="exercise.id"
                :disabled="inSelected(exercise.id)"
                color="darkGrey"
                dark 
              >
                {{ exercise.name }} 
                <v-icon 
                  right
                  @click.stop="selectExercise(exercise)"
                >add_circle</v-icon>
              </v-chip>
            </v-flex>

            <v-flex 
              mt-3
              mr-3 
              ml-3>
              <p class="subheading grey--text text--darken-2"> Popular exercises are
              intelligently selected across all users with a bias towards your workout habits.</p>
            </v-flex>
          </v-flex>

          <v-flex 
            xs12 
            mt-3>
            <v-subheader>Search exercises</v-subheader>
            <v-form class="mr-3 ml-3">
              <v-autocomplete
                v-model="newExercises"
                :items="exerciseTypes"
                placeholder="ex. Benchpress"
                browser-autcomplete
                clearable
                chips
                deletable-chips
                hint
                multiple
                small-chips
                solo
                color="primary"
                light
              />
            </v-form>
            <v-flex 
              mr-3 
              ml-3>
              <p class="subheading grey--text text--darken-2">Search across all exercises. If you can't find what you're
              looking for you can add a custom exercise as well.</p>
            </v-flex>
          </v-flex>

        </v-layout>
      </v-card>
    </v-dialog>
  </v-flex>
</template>

<script>
import { mutations } from "@/graphql";
import { showSnackbar } from "@/helpers";

export default {
  name: "CreateWorkout",

  data() {
    return {
      loading: false,
      dialog: false,
      exerciseTypes: [],
      newExercises: [],
      selectedExercises: [
        { id: 1, name: "Barbell Benchpress" },
        { id: 2, name: "Barbell Squat" },
        { id: 3, name: "Row" },
        { id: 4, name: "Chin-up" }
      ],
      popularExercises: [{ id: 5, name: "Shoulder Press" }]
    };
  },

  methods: {
    inSelected(exerciseId) {
      return Boolean(this.selectedExercises.find(ex => ex.id === exerciseId));
    },

    selectExercise(exercise) {
      if (this.inSelected(exercise.id)) {
        return;
      }
      this.selectedExercises = [exercise, ...this.selectedExercises];
    },

    deselectExercise(exerciseId) {
      this.selectedExercises = this.selectedExercises.filter(
        ex => ex.id !== exerciseId
      );
    },

    createWorkout() {
      this.loading = true;

      this.$apollo
        .mutate({
          mutation: mutations.createWorkoutMutation

          /*
          update: (store, { data }) => {
            const newWorkout = data.createWorkout.workout;
            const result = store.readQuery({
              query: queries.workoutsQuery
            });

            // Prepend the latest workout
            result.workouts.unshift(newWorkout);

            store.writeQuery({
              query: queries.workoutsQuery,
              data: result
            });
          }
          */
        })
        .then(resp => {
          const workout = resp.data.createWorkout.workout;

          this.loading = false;

          showSnackbar("success", "New workout created.");

          this.$router.push({
            name: "Workout",
            params: { workoutId: workout.id }
          });
        })
        .catch(() => {
          this.loading = false;

          showSnackbar(
            "error",
            "Oops, there seems to be a problem, support has been notified."
          );
        });
    }
  }
};
</script>
