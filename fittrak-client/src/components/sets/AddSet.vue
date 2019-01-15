<template>
  <v-form>
    <v-flex>
      <v-text-field 
        v-model="repetitions" 
        placeholder="Repetitions" 
        type="number" />
    </v-flex>

    <v-flex>
      <v-text-field 
        v-model="weight" 
        placeholder="Weight" 
        type="number" />
    </v-flex>

    <v-flex xs12>
      <v-radio-group 
        v-model="unit" 
        row>
        <v-radio 
          color="primary" 
          label="LB" 
          value="LB" />
        <v-radio 
          color="primary" 
          label="KG" 
          value="KG" />
      </v-radio-group>
    </v-flex>

    <v-flex xs12>
      <v-checkbox 
        v-model="bodyweight" 
        label="Using bodyweight"/>
    </v-flex>

    <v-flex 
      xs12 
      text-xs-right>
      <v-btn 
        depressed 
        color="secondary" 
        @click.stop="addSet">Add</v-btn>
    </v-flex>
  </v-form>
</template>

<script>
import { queries, mutations } from "@/graphql";

import { showSnackbar } from "@/helpers";

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
          mutation: mutations.addSetMutation,

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
              query: queries.setsQuery,
              variables: {
                exerciseId: exercise.id
              }
            });

            result.sets = [set, ...result.sets];

            store.writeQuery({
              query: queries.setsQuery,
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

          showSnackbar("success", "Set added.");
        })
        .catch(() => {
          showSnackbar(
            "error",
            "Could not add set. Support has been notified."
          );
        });
    }
  },

  props: {
    exercise: {
      type: Object,
      required: true
    }
  }
};
</script>
