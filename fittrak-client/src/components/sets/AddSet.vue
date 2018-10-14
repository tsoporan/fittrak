<template>
  <v-form>
    <v-text-field v-model="repetitions" placeholder="Repetitions" type="number" />
    <v-text-field v-model="weight" placeholder="Weight" type="number" />

    <v-radio-group v-model="unit" row>
      <v-radio color="primary" label="LB" value="LB" />
      <v-radio color="primary" label="KG" value="KG" />
    </v-radio-group>

    <v-checkbox v-model="bodyweight" label="Using bodyweight"></v-checkbox>

    <v-btn depressed color="secondary" @click.stop="addSet">Add</v-btn>
  </v-form>
</template>

<script>
import AddSetMutation from "@/graphql/mutations/addSet.graphql";
import SetsQuery from "@/graphql/queries/sets.graphql";

import { EventBus } from "@/helpers";

export default {
  name: "AddSet",

  data() {
    return {
      repetitions: "",
      weight: "",
      unit: "LB",
      bodyweight: false
    };
  },

  methods: {
    addSet() {
      const { exercise } = this.$props;
      const { repetitions, weight, unit, bodyweight } = this;

      if (!(repetitions && weight && unit)) return;

      this.$apollo
        .mutate({
          mutation: AddSetMutation,

          variables: {
            exerciseId: exercise.id,
            repetitions,
            weight,
            unit,
            bodyweight
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
          this.bodyweight = false;

          EventBus.$emit("show-snackbar", {
            type: "success",
            text: "Set added."
          });
        })
        .catch(() => {
          EventBus.$emit("show-snackbar", {
            type: "error",
            text: "Could not add set. Support has been notified."
          });
        });
    }
  },

  props: {
    exercise: Object
  }
};
</script>
