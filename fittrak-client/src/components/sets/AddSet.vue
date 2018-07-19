<template>
  <form>
    <div class="field is-grouped">
      <p class="control">
        <input class="input" v-model="repetitions" type="text" placeholder="Repetitions" />
      </p>

      <p class="control">
        <input class="input" v-model="weight" type="text" placeholder="Weight" />
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

      <p class="control">
        <button class="button is-primary" v-on:click.prevent="addSet">Add Set</Button>
      </p>
    </div>
  </form>
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
