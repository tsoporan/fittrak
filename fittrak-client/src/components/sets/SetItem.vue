<template>
<v-list-tile v-if="!editing">
    <v-list-tile-content>
      <v-list-tile-title>{{ set.repetitions }} x {{ set.weight }} {{ set.unit }}</v-list-tile-title>
    </v-list-tile-content>

    <v-list-tile-action>
      <v-btn small flat color="info" icon @click.stop="editSet">
        <v-icon>edit</v-icon>
      </v-btn>
    </v-list-tile-action>

    <v-list-tile-action>
      <v-btn small flat color="info" icon @click.stop="removeSet">
        <v-icon>delete</v-icon>
      </v-btn>
    </v-list-tile-action>
</v-list-tile>
<v-flex v-else>
  <v-layout row wrap>
    <v-flex>
      <v-text-field v-model="repetitions" placeholder="Reps" type="number" />
    </v-flex>

    <v-flex>
      <v-text-field v-model="weight" placeholder="Weight" type="number" />
    </v-flex>

    <v-flex mt-2>
      <v-radio-group v-model="unit" row class="mt-3">
        <v-radio color="primary" label="LB" value="LB" />
        <v-radio color="primary" label="KG" value="KG" />
      </v-radio-group>
    </v-flex>

    <v-flex xs12 text-xs-right>
      <v-btn small depressed color="gray" @click.stop="editing = false">Cancel</v-btn>
      <v-btn small depressed color="success" @click.stop="updateSet">Save</v-btn>
    </v-flex>
  </v-layout>

</v-flex>
</template>

<script>
import SetsQuery from "@/graphql/queries/sets.graphql";
import UpdateSetMutation from "@/graphql/mutations/updateSet.graphql";
import RemoveSetMutation from "@/graphql/mutations/removeSet.graphql";

export default {
  name: "SetItem",

  data() {
    return {
      editing: false,
      weight: this.$props.set.weight,
      repetitions: this.$props.set.repetitions,
      unit: this.$props.set.unit
    };
  },

  methods: {
    editSet() {
      this.editing = true;
    },

    removeSet() {
      const { set } = this.$props;

      this.$apollo.mutate({
        mutation: RemoveSetMutation,
        variables: {
          setId: set.id
        },
        update(store, { data }) {
          const set = data.removeSet.set;

          const result = store.readQuery({
            query: SetsQuery,
            variables: {
              exerciseId: set.exercise.id
            }
          });

          result.sets = result.sets.filter(s => s.id !== set.id);

          store.writeQuery({
            query: SetsQuery,
            variables: {
              exerciseId: set.exercise.id
            },
            data: result
          });
        }
      });
    },

    updateSet() {
      const { set } = this.$props;

      this.$apollo
        .mutate({
          mutation: UpdateSetMutation,
          variables: {
            setId: set.id,
            setFields: {
              weight: this.weight,
              repetitions: this.repetitions,
              unit: this.unit
            }
          }
        })
        .then(() => {
          this.editing = false;
        });
    }
  },

  props: {
    set: Object
  }
};
</script>
