<template>
<v-layout justify-center row wrap>
  <StartWorkout></StartWorkout>
  <RecentWorkouts></RecentWorkouts>
</v-layout>
</template>

<script>
import moment from 'moment'
import StartWorkout from './workouts/StartWorkout'
import RecentWorkouts from './workouts/RecentWorkouts'

export default {
  data: () => ({
    today: moment().format('MMMM Do, YYYY')
  }),

  components: {
    StartWorkout,
    RecentWorkouts
  }
}
</script>

