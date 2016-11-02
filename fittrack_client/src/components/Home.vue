<template>
  <div>
    <h2> It's {{ today }} </h2>
    <router-link to="/startworkout" class="button is-large is-primary is-outlined">New Workout</router-link>
  </div>

</template>

<style>
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

