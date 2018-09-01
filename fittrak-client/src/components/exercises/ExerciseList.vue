<template>
  <v-expansion-panel v-if="workout.exercises.length">
    <v-expansion-panel-content
      v-for="exercise in workout.exercises"
      :key="exercise.id"
      >
      <div slot="header">
        <strong>{{ exercise.name }} </strong>
        <RemoveExercise :exercise=exercise />
      </div>

      <v-card>
        <v-divider />

        <v-flex ma-4>
          <p>ID: #{{ exercise.id }}</p>
          <h2 class="display-0"> Add Set </h2>
          <AddSet :exercise=exercise />
        </v-flex>

          <v-divider />
        <v-flex ma-4>
          <p></p>
          <h2 class="display-0"> Set List </h2>
          <SetList :exercise=exercise />
        </v-flex>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
  <v-flex v-else text-xs-center>
    No exercises! 😞
  </v-flex>
</template>

<script>
import AddSet from "@/components/sets/AddSet";
import SetList from "@/components/sets/SetList";
import RemoveExercise from "@/components/exercises/RemoveExercise";

export default {
  name: "ExerciseList",

  components: {
    AddSet,
    SetList,
    RemoveExercise
  },

  props: {
    workout: Object
  }
};
</script>
