<template>
  <v-card 
    flat 
    color="main_bg"> 
    <v-card-title>
      <span class="headline grey--text text--darken-2">Latest</span>
      <v-spacer />
      <v-menu 
        bottom 
        left>
        <v-btn 
          slot="activator" 
          dark 
          icon>
          <v-icon 
            color="grey darken-2">filter_list</v-icon>
        </v-btn>
      </v-menu>
    </v-card-title>
  </v-card>
</template>

<script>
export default {
  name: "WorkoutFilterHeader"
};
</script>
