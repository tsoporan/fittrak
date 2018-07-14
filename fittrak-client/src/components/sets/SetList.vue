<template>
  <div>
    <h3>Set List</h3>
    <ul v-if="activeSets.length">
      <SetItem
        v-for="set in activeSets"
        :key="set.id"
        :set="set"
      />
    </ul>
    <p v-else> 
      No sets!
    </p>
  </div>
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
