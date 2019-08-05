<template>
  <v-toolbar flat>
    <v-toolbar-title>
      <span class="headline grey--text text--darken-2">{{
        currentFilter
      }}</span>
    </v-toolbar-title>

    <v-spacer />

    <v-toolbar-items>
      <v-menu bottom left>
        <v-btn slot="activator" dark icon>
          <v-icon color="grey darken-2">filter_list</v-icon>
        </v-btn>
      </v-menu>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
export default {
  name: "WorkoutFilterToolbar",
  data() {
    return {
      currentFilter: "Latest"
    };
  }
};
</script>
