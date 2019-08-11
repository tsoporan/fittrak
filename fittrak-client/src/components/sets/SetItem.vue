<template>
  <v-list-item inactive v-if="!editing" style="width:100%">
    <v-list-item-content>
      <v-list-item-title>
        {{ repetitions }} x {{ weight }} {{ unit }}
      </v-list-item-title>

      <v-list-item-subtitle v-if="!bodyweight">
        {{ repetitions * weight }} {{ unit }}s
      </v-list-item-subtitle>
      <v-list-item-subtitle v-else>Body weight</v-list-item-subtitle>
    </v-list-item-content>
    <v-list-item-action @click.stop="editSet" style="cursor:pointer">
      <v-icon color="blue">edit</v-icon>
    </v-list-item-action>
    <v-list-item-action @click.stop="removeSet" style="cursor:pointer">
      <v-icon color="red lighten-1">delete</v-icon>
    </v-list-item-action>
  </v-list-item>

  <v-list-item v-else>
    <v-layout row wrap pl-4 pr-4 pb-5>
      <v-flex xs12>
        <v-text-field v-model="repetitions" placeholder="Reps" type="number" />
      </v-flex>

      <v-flex xs12>
        <v-text-field v-model="weight" placeholder="Weight" type="number" />
      </v-flex>

      <v-flex xs12>
        <v-radio-group v-model="unit" row class="mt-3">
          <v-radio color="primary" label="LB" value="LB" />
          <v-radio color="primary" label="KG" value="KG" />
        </v-radio-group>
      </v-flex>

      <v-flex xs12>
        <v-checkbox
          v-model="bodyweight"
          color="primary"
          label="Using bodyweight"
        />
      </v-flex>

      <v-flex xs12 text-end>
        <v-btn
          small
          rounded
          color="grey lighten-2"
          @click.stop="editing = false"
          >Cancel</v-btn
        >
        <v-btn
          class="ml-2"
          small
          rounded
          dark
          color="darkGrey"
          @click.stop="updateSet"
          >Save</v-btn
        >
      </v-flex>
    </v-layout>
  </v-list-item>
</template>

<script>
import { queries, mutations } from "@/graphql";

import { showSnackbar } from "@/helpers";

export default {
  name: "SetItem",

  data() {
    const { set } = this.$props;

    return {
      editing: false,
      weight: set.weight,
      repetitions: set.repetitions,
      unit: set.unit,
      bodyweight: set.bodyweight
    };
  },

  computed: {
    /*
    isSetDone: function() {
      const set = this.$props;

      return set.status === SET_DONE;
    }
    */
  },

  methods: {
    editSet() {
      this.editing = true;
    },

    removeSet() {
      const set = this.set;

      this.$apollo
        .mutate({
          mutation: queries.RemoveSetMutation,
          variables: {
            setId: set.id
          },
          update(store, { data }) {
            const set = data.removeSet.set;

            const result = store.readQuery({
              query: queries.SetsQuery,
              variables: {
                exerciseId: set.exercise.id
              }
            });

            result.sets = result.sets.filter(s => s.id !== set.id);

            store.writeQuery({
              query: queries.SetsQuery,
              variables: {
                exerciseId: set.exercise.id
              },
              data: result
            });
          }
        })
        .then(() => {
          showSnackbar("success", "Set removed");
        })
        .catch(() => {
          showSnackbar(
            "error",
            "Could not remove Set. Support has been notified."
          );
        });
    },

    updateSet() {
      const set = this.set;
      const { weight, unit, repetitions, bodyweight } = this;

      this.$apollo
        .mutate({
          mutation: mutations.updateSetMutation,
          variables: {
            setId: set.id,
            setFields: {
              weight,
              repetitions,
              unit,
              bodyweight
            }
          }
        })
        .then(() => {
          this.editing = false;

          showSnackbar("success", "Set updated.");
        })
        .catch(() => {
          showSnackbar(
            "error",
            "Could not update Set. Support has been notified."
          );
        });
    }
  },

  props: {
    set: {
      type: Object,
      required: true
    }
  }
};
</script>
