<template>
  <v-expansion-panel v-if="activeExercises.length">
    <v-expansion-panel-content
      v-for="exercise in activeExercises"
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
  <p v-else>
    No exercises!
  </p>
</template>

<script>
import AddSet from "@/components/sets/AddSet";
import SetList from "@/components/sets/SetList";
import RemoveExercise from "@/components/exercises/RemoveExercise";

export default {
  name: "ExerciseList",

  computed: {
    activeExercises() {
      const { workout } = this.$props;

      if (!workout) return [];

      return workout.exercises.filter(e => e.isActive);
    }
  },

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

<style scoped>
</style>
