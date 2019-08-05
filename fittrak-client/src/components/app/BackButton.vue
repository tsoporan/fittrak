<template>
  <v-flex>
    <v-btn @click.stop="goBack" flat color="secondary" outline>Back</v-btn>
  </v-flex>
</template>

<script>
export default {
  name: "BackButton",
  methods: {
    goBack() {
      return this.$router.go(-1);
    }
  }
};
</script>
