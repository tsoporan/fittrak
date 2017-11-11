<template>
<v-layout justify-center row wrap>
  <StartWorkout></StartWorkout>
  <LatestWorkouts></LatestWorkouts>
</v-layout>
</template>

<script>
import moment from 'moment'
import StartWorkout from './workouts/StartWorkout'
import LatestWorkouts from './workouts/LatestWorkouts'

export default {
  data: () => ({
    today: moment().format('MMMM Do, YYYY')
  }),

  components: {
    StartWorkout,
    LatestWorkouts
  }
}
</script>

