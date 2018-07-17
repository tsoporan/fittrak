<template>
  <li>
    ID: {{ set.id }}
    Weight:
    <input v-if="editing" v-model="weight" type="text" /> <p v-else>{{ set.weight }} {{ unit }}</p>
    Reps:
    <input v-if="editing" v-model="repetitions" type="text" /> <p v-else>{{ set.repetitions }}</p>

    <div v-if="editing">
      <input v-model="unit" type="radio" id="kg" name="unit" value="KG" />
      <label for="kg">KGs</label>
      <input v-model="unit" type="radio" id="lb" name="unit" checked value="LB" />
      <label for="lb">LBs</label>
    </div>

    <hr />

    <RemoveSet :set=set />

    <button v-if="!editing" v-on:click.prevent="editSet">Edit</button>
    <button v-else v-on:click.prevent="updateSet">Save</button>
  </li>
</template>

<script>
import RemoveSet from "@/components/sets/RemoveSet";

import UPDATE_SET from "@/graphql/mutations/updateSet.graphql";

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

    updateSet() {
      const { set } = this.$props;

      this.$apollo
        .mutate({
          mutation: UPDATE_SET,
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

  components: {
    RemoveSet
  },

  props: {
    set: Object
  }
};
</script>

<style scoped>
li {
  margin: 10px;
}
</style>
