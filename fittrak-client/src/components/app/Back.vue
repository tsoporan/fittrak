<template>
  <v-btn @click.stop="goBack" flat color="secondary" outline>Back</v-btn>
</template>

<script>
export default {
  name: "Back",
  methods: {
    goBack() {
      return this.$router.go(-1);
    }
  }
};
</script>
