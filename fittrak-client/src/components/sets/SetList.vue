<template>
  <v-list v-if="activeSets.length">
    <v-list-tile
      v-for="set in activeSets"
      :key="set.id"
      :set="set"
    >
      <v-list-tile-content>
        <v-list-tile-title>{{ set.repetitions }} x {{ set.weight }} {{ set.unit }}</v-list-tile-title>
      </v-list-tile-content>

      <v-list-tile-action>
        <v-icon>edit</v-icon>
      </v-list-tile-action>

      <v-list-tile-action>
        <v-icon>delete</v-icon>
      </v-list-tile-action>

    </v-list-tile>
  </v-list>

  <p v-else>
    No sets!
  </p>
</template>

<script>
import SetItem from "@/components/sets/SetItem.vue";
import EXERCISE from "@/graphql/queries/exercise.graphql";

export default {
  name: "SetList",
  data() {
    return {
      sets: [],
      exerciseId: this.$props.exercise.id
    };
  },

  apollo: {
    sets: {
      query: EXERCISE,

      variables() {
        return {
          exerciseId: this.$props.exercise.id
        };
      },

      update: data => data.exercise.sets
    }
  },

  computed: {
    activeSets() {
      return this.sets.filter(set => set.isActive);
    }
  },

  components: {
    SetItem
  },

  props: {
    exercise: Object
  }
};
</script>
