<template>
  <div style="height:100%">
    <AppBar title="Build workout" />

    <v-container fluid>
      <v-layout row mb-12 ma-1>
        <v-flex>
          <v-card>
            <v-card-text>
              💡 Build your workout below! Once you're ready
              <kbd>start</kbd> your workout. Not yet ready to start? Place your
              workout on <kbd>hold</kbd> and come back to it later!
            </v-card-text>
          </v-card>
        </v-flex>

        <v-flex xs12 pt-5>
          <div>
            <span class="title">🔍 Search</span>
            <span class="caption"> &mdash; tailored for you 🤓</span>
          </div>
          <v-flex pt-3>
            <v-form>
              <v-autocomplete
                v-model="searchSelectedExercises"
                :items="exerciseTypes"
                item-text="name"
                item-value="name"
                placeholder="Type an exercise ex. Bench press"
                browser-autcomplete
                clearable
                chips
                deletable-chips
                multiple
                small-chips
                outlined
                flat
                full-width
                dense
                @blur="addMultiSelected"
              >
                <template v-slot:no-data>
                  Hrm, that exercise doesn't exist.
                </template>
              </v-autocomplete>
            </v-form>

            <!--
            TODO: Can this be done in the input on
            a non found exercise?
          <v-flex text-xs-right mr-3 ml-3>
            <v-btn rounded dark>Add custom </v-btn>
          -->
          </v-flex>
        </v-flex>

        <v-flex xs12 pt-2 pb-2>
          <div>
            <span class="title">⭐ Quick picks</span>
            <span class="caption"> &mdash; intelligently chosen 🔮</span>
          </div>
          <v-flex v-if="popularExerciseTypes.length" mr-2 ml-2>
            <v-chip-group multiple column dark color="darkGrey">
              <v-chip
                small
                v-for="exercise in popularExerciseTypes"
                :key="exercise.id"
                :disabled="inSelected(exercise.id)"
              >
                {{ exercise.name }}
                <v-icon
                  dark
                  color="grey"
                  right
                  @click.stop="selectExercise(exercise)"
                  >add_circle</v-icon
                >
              </v-chip>
            </v-chip-group>
          </v-flex>
        </v-flex>

        <v-flex xs12 pt-5 pb-2>
          <div>
            <span class="title">💚 Your workout</span>
            <span class="caption"> &mdash; ready, set, 💪!</span>
          </div>
          <v-flex v-if="selectedExercises.length" mb-4 mr-2 ml-2>
            <v-chip-group multiple column dark>
              <v-chip
                small
                :key="exercise.id"
                v-for="exercise in selectedExercises"
                color="primary"
              >
                {{ exercise.name }}
                <v-icon right @click.stop="deselectExercise(exercise.id)"
                  >cancel</v-icon
                >
              </v-chip>
            </v-chip-group>
          </v-flex>
          <v-flex v-else mr-3 ml-3>
            <p class="subheading grey--text text--darken-2">
              No exercises selected yet!
            </p>
          </v-flex>
        </v-flex>
      </v-layout>

      <WorkoutFooter>
        <v-btn color="darkGrey" @click.stop="cancelWorkout" icon>
          <v-icon>cancel</v-icon>
        </v-btn>

        <v-btn color="darkGrey" @click.stop="pauseWorkout" icon>
          <v-icon>pause</v-icon>
        </v-btn>

        <v-btn color="darkGrey" @click.stop="startWorkout" icon>
          <v-icon>play_arrow</v-icon>
        </v-btn>
      </WorkoutFooter>
    </v-container>
  </div>
</template>

<script>
import { queries, mutations } from "@/graphql";
import { showSnackbar } from "@/helpers";

import { IN_PROGRESS } from "@/constants";

import AppBar from "@/components/app/AppBar";
import WorkoutFooter from "@/components/workouts/WorkoutFooter";

export default {
  name: "WorkoutSetup",

  data() {
    return {
      loading: false,
      dialog: false,
      exerciseTypes: [],
      searchSelectedExercises: [],
      selectedExercises: [],
      popularExerciseTypes: [],
      workout: {}
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

    exerciseTypes: {
      query: queries.exerciseTypesQuery,

      update(data) {
        return data.exerciseTypes;
      }
    },

    popularExerciseTypes: {
      query: queries.popularExerciseTypesQuery
    }
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

    addMultiSelected() {
      const selectedWithIds = this.searchSelectedExercises.map(name => {
        const item = this.exerciseTypes.find(item => item.name === name);

        return {
          name,
          id: item.id
        };
      });

      this.selectedExercises = [...selectedWithIds, ...this.selectedExercises];

      this.searchSelectedExercises = [];
    },

    startWorkout() {
      const workout = this.workout;

      if (!this.selectedExercises.length) {
        showSnackbar("orange", "Uh-oh looks like you have no exercises added.");
        return;
      }

      if (!(workout && workout.id)) {
        showSnackbar(
          "error",
          "Hmm seems like there isn't an attached work out. Please create again.",
          true
        );
        return;
      }

      // Ensure matches the input type
      const normalizedSelected = this.selectedExercises.map(exercise => ({
        id: exercise.id,
        name: exercise.name
      }));

      this.$apollo
        .mutate({
          mutation: mutations.updateWorkoutMutation,

          variables: {
            workoutId: workout.id,
            workoutFields: {
              dateStarted: new Date(),
              status: IN_PROGRESS,
              exerciseTypes: normalizedSelected
            }
          }
        })
        .then(() => {
          this.selectedExercises = [];
          showSnackbar("success", "Workout started!");
        })
        .catch(() => {
          showSnackbar("error", "Could not start workout.", true);
        });
    },

    cancelWorkout() {
      console.log("cancelling workout");
    },

    pauseWorkout() {
      console.log("pausing workout");
    }
  },

  components: {
    AppBar,
    WorkoutFooter
  }
};
</script>
