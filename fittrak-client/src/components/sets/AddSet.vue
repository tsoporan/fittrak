<template>
  <div>
    <form>
      <input v-model="repetitions" type="text" placeholder="Repetitions" />
      <input v-model="weight" type="text" placeholder="Weight" />
      <div>
        Units:
        <input v-model="unit" type="radio" id="kg" name="unit" value="KG" />
        <label for="kg">KGs</label>
        <input v-model="unit" type="radio" id="lb" name="unit" checked value="LB" />
        <label for="lb">LBs</label>
      </div>
      <button v-on:click.prevent="addSet">Add Set</Button>
    </form>
  </div>
</template>

<script>
import ADD_SET from "@/graphql/mutations/addSet.graphql";

export default {
  name: "AddSet",

  data() {
    return {
      repetitions: "",
      weight: "",
      unit: ""
    };
  },

  methods: {
    addSet() {
      const { exercise } = this.$props;
      const { repetitions, weight, unit } = this;

      if (!(repetitions && weight && unit)) return;

      this.$apollo
        .mutate({
          mutation: ADD_SET,

          variables: {
            exerciseId: exercise.id,
            repetitions,
            weight,
            unit
          }
        })
        .then(() => {
          // Clear out for next entry
          this.repetitions = "";
          this.weight = "";
        });
    }
  },

  props: {
    exercise: Object
  }
};
</script>

<style scoped>
form {
  padding: 5px;
}
input {
  margin: 5px;
}
</style>
