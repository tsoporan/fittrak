<template>
  <v-form>
    <v-text-field v-model="repetitions" placeholder="Repetitions" />
    <v-text-field v-model="weight" placeholder="Weight" />

    <v-radio-group v-model="unit" row>
      <v-radio color="primary" label="LB" value="LB" />
      <v-radio color="primary" label="KG" value="KG" />
    </v-radio-group>

    <v-btn depressed color="secondary" @click.stop="addSet">Add Set</v-btn>
  </v-form>
</template>

<script>
import ADD_SET from "@/graphql/mutations/addSet.graphql";

export default {
  name: "AddSet",

  data() {
    return {
      repetitions: "",
      weight: "",
      unit: "LB"
    };
  },

  methods: {
    addSet() {
      const { exercise } = this.$props;
      const { repetitions, weight, unit } = this;

      if (!(repetitions && weight && unit)) return;

      this.$apollo
        .mutate({
          mutation: ADD_SET,

          variables: {
            exerciseId: exercise.id,
            repetitions,
            weight,
            unit
          }
        })
        .then(() => {
          // Clear out for next entry
          this.repetitions = "";
          this.weight = "";
        });
    }
  },

  props: {
    exercise: Object
  }
};
</script>

<style scoped>
</style>
