<template>
<v-layout justify-center row wrap>
  <WorkoutActions></WorkoutActions>
  <RecentWorkouts></RecentWorkouts>
</v-layout>
</template>

<script>
import moment from 'moment'
import WorkoutActions from './workouts/WorkoutActions'
import RecentWorkouts from './workouts/RecentWorkouts'

export default {
  data: () => ({
    today: moment().format('MMMM Do, YYYY')
  }),

  components: {
    WorkoutActions,
    RecentWorkouts
  }
}
</script>
