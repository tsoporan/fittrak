<template>
  <v-list v-if="sets.length">
    <SetItem
      v-for="set in sets"
      :key="set.id"
      :set="set"
    />
  </v-list>

  <p v-else>
    No sets!
  </p>
</template>

<script>
import SetsQuery from "@/graphql/queries/sets.graphql";

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

  components: {
    SetItem
  },

  props: {
    exercise: {
      type: Object,
      required: true
    }
  }
};
</script>
