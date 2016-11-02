<template>
  <div class="new-workout">
    <h2> It's {{ today }} </h2>
    <router-link to="/newworkout" class="button is-large is-primary is-outlined">New Workout</router-link>
  </div>

</template>

<style lang="scss" scoped>

div.new-workout {
  text-align: center;
}

div.new-workout h2 {
  padding: 2rem;
}

</style>

<script>
import moment from 'moment'

export default {
  data () {
    return {
      today: moment().format('MMMM Do, YYYY')
    }
  }
}
</script>

