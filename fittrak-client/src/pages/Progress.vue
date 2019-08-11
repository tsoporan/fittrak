<template>
  <div>
    <AppBar title="Progress" />
    <v-container>
      <v-layout row wrap>
        <v-flex xs12>
          <p>Nothing to see here.</p>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import AppBar from "@/components/app/AppBar";

export default {
  name: "Progress",
  components: {
    AppBar
  }
};
</script>

<style scoped></style>
