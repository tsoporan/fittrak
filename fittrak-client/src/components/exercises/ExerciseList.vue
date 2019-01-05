<template>
  <v-flex xs12>
    <v-expansion-panel 
      v-if="exercises && exercises.length" 
      expand 
      v-model="panel">
      <v-expansion-panel-content
        v-for="exercise in exercises"
        :key="exercise.id"
      >
        <v-flex slot="header">
          <strong>{{ exercise.name }} </strong>
        </v-flex>

        <v-card>
          <v-divider />

          <v-flex ma-4>
            <v-layout 
              row 
              wrap>
              <v-flex text-xs-right>
                <v-btn 
                  small 
                  flat 
                  color="info" 
                  icon 
                  @click.stop="removeExercise(exercise)">
                  <v-icon>delete</v-icon>
                </v-btn>
              </v-flex>
            </v-layout>

            <h2 class="display-0"> Add Set </h2>
            <AddSet :exercise="exercise" />
          </v-flex>

          <v-divider />

          <v-flex ma-4>
            <p/>
            <h2 class="display-0"> Set List </h2>
            <SetList :exercise="exercise" />
          </v-flex>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-flex 
      v-else 
      text-xs-center>
      No exercises! 😞
    </v-flex>
  </v-flex>
</template>

<script>
import RemoveExerciseMutation from "@/graphql/mutations/removeExercise.graphql";
import ExercisesQuery from "@/graphql/queries/exercises.graphql";

import AddSet from "@/components/sets/AddSet";
import SetList from "@/components/sets/SetList";

export default {
  name: "ExerciseList",

  data() {
    return {
      panel: [true]
    };
  },

  methods: {
    removeExercise(exercise) {
      this.$apollo.mutate({
        mutation: RemoveExerciseMutation,
        variables: {
          exerciseId: exercise.id
        },
        update(store) {
          const result = store.readQuery({
            query: ExercisesQuery,
            variables: {
              workoutId: exercise.workout.id
            }
          });

          result.exercises = result.exercises.filter(
            current => exercise.id !== current.id
          );

          store.writeQuery({
            query: ExercisesQuery,
            variables: {
              workoutId: exercise.workout.id
            },
            data: result
          });
        }
      });
    }
  },

  components: {
    AddSet,
    SetList
  },

  props: {
    exercises: Array
  }
};
</script>
