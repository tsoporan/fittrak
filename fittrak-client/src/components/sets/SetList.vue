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
import { queries } from "@/graphql";

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
      query: queries.setsQuery,
      variables() {
        const exercise = this.exercise;

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
