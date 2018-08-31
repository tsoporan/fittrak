<template>
  <li>
    <p>ID: {{ set.id }}</p>

    <div v-if="editing">
      <div class="field is-grouped">
        <p class="control">
          <input class="input" v-if="editing" v-model="weight" type="text" />
        </p>

        <p class="control">
          <input class="input" v-if="editing" v-model="repetitions" type="text" />
        </p>

        <p class="control">
          <label class="radio">
            <input type="radio" name="unit" v-model="unit" checked id="lb" value="LB">
            LBs
          </label>
          <label class="radio">
            <input type="radio" name="unit" v-model="unit" id="kg" value="KG">
            KGs
          </label>
        </p>

        <div class="control">
          <button class="button is-primary" v-on:click.prevent="updateSet">Save</button>
        </div>
      </div>
    </div>

    <div v-else>
      <p>Weight: {{ set.weight }} {{ set.unit }}</p>
      <p>Repetitions: {{ set.repetitions }}</p>
    </div>

    <hr />

    <div class="field is-grouped">
      <p class="control">
        <RemoveSet :set=set />
      </p>

      <p class="control">
        <button class="button" v-if="!editing" v-on:click.prevent="editSet">Edit</button>
      </p>
    </div>
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
