<template>
  <div>
    <button v-on:click.prevent="removeSet">Remove Set</button>
  </div>
</template>

<script>
import REMOVE_SET from "@/graphql/mutations/removeSet.graphql";

export default {
  name: "RemoveSet",

  methods: {
    removeSet() {
      const { set } = this.$props;

      this.$apollo.mutate({
        mutation: REMOVE_SET,
        variables: {
          setId: set.id
        }
      });
    }
  },

  props: {
    set: Object
  }
};
</script>
