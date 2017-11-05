<template>
<div class="container">
  <div class="new-workout">
    <router-link to="/workouts/start" class="button is-large is-primary is-outlined">New Workout</router-link>
  </div>

  <StartedWorkouts></StartedWorkouts>
  <LatestWorkouts></LatestWorkouts>
</div>
</template>

<style lang="scss" scoped>
$white: #ffffff;
$lgrey: #e2e2e2;

div.container {
  margin: 2rem 1rem;
}

div.new-workout {
  text-align: center;
  padding-bottom: 2rem;
}

div.new-workout h2 {
  padding: 2rem;
}
</style>

<script>
import moment from 'moment'
import StartedWorkouts from './StartedWorkouts'
import LatestWorkouts from './LatestWorkouts'

export default {
  data () {
    return {
      startedWorkouts: true,
      today: moment().format('MMMM Do, YYYY')
    }
  },
  components: {
    StartedWorkouts,
    LatestWorkouts
  }
}
</script>

