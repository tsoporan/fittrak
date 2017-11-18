<template>
<v-flex class="text-xs-center">
  <v-btn
    @click.stop="$router.push('/workouts/start/')"
    dark
    >
    Start Workout
  </v-btn>

  <v-btn
    disabled
    @click.prevent="">
    Start Routine 
  </v-btn>
</v-flex>
</template>

<script>

export default {

}
</script>
