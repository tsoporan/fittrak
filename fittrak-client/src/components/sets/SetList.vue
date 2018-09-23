<template>
  <v-list v-if="sets.length">
    <v-list-tile
      v-for="set in sets"
      :key="set.id"
      :set="set"
    >
      <v-list-tile-content>
        <v-list-tile-title>{{ set.repetitions }} x {{ set.weight }} {{ set.unit }}</v-list-tile-title>
      </v-list-tile-content>

      <v-list-tile-action>
        <v-btn small flat color="info" icon @click.stop="editSet(set)">
          <v-icon>edit</v-icon>
        </v-btn>
      </v-list-tile-action>

      <v-list-tile-action>
        <v-btn small flat color="info" icon @click.stop="removeSet(set)">
          <v-icon>delete</v-icon>
        </v-btn>
      </v-list-tile-action>

    </v-list-tile>
  </v-list>

  <p v-else>
    No sets!
  </p>
</template>

<script>
import SetsQuery from "@/graphql/queries/sets.graphql";
import RemoveSetMutation from "@/graphql/mutations/removeSet.graphql";

import SetItem from "@/components/sets/SetItem.vue";

export default {
  name: "SetList",

  data() {
    return {
      sets: []
    };
  },

  apollo: {
    sets: {
      query: SetsQuery,
      variables() {
        const { exercise } = this.$props;

        return {
          exerciseId: exercise.id
        };
      }
    }
  },

  methods: {
    removeSet(set) {
      const { exercise } = this.$props;

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
              exerciseId: exercise.id
            }
          });

          result.sets = result.sets.filter(s => s.id !== set.id);

          store.writeQuery({
            query: SetsQuery,
            variables: {
              exerciseId: exercise.id
            },
            data: result
          });
        }
      });
    },

    editSet(set) {}
  },

  components: {
    SetItem
  },

  props: {
    exercise: Object
  }
};
</script>
