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

export default {
  name: "SetList",

  components: {
    SetItem
  },

  props: {
    sets: Array
  }
};
</script>
