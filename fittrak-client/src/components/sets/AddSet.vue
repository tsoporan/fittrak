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
import AddSetMutation from "@/graphql/mutations/addSet.graphql";
import SetsQuery from "@/graphql/queries/sets.graphql";

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
          mutation: AddSetMutation,

          variables: {
            exerciseId: exercise.id,
            repetitions,
            weight,
            unit
          },

          update(store, { data }) {
            const set = data.addSet.set;

            const result = store.readQuery({
              query: SetsQuery,
              variables: {
                exerciseId: exercise.id
              }
            });

            result.sets = [set, ...result.sets];

            store.writeQuery({
              query: SetsQuery,
              variables: {
                exerciseId: exercise.id
              },
              data: result
            });
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
