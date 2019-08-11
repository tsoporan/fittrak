<template>
  <v-container grid-list-xl fluid>
    <v-layout row>
      <v-list two-line flat v-if="sets.length" style="width:100%">
        <SetItem v-for="set in sets" :key="set.id" :set="set" />
      </v-list>

      <v-flex v-else text-center>
        No sets yet 😔
      </v-flex>
    </v-layout>
  </v-container>
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
