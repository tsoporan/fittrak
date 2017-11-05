<template>
<div class="latest-workouts">
  <h3> Latest Workouts </h3>
  <div v-if="hasLatest">
    <ul>
      <li v-for="w in latestWorkouts">
        <router-link :to="{ name: 'workout-detail', params: { workoutSlug: w.slug }}">
          <h4>Workout</h4>
          <p>
            Started: {{ w.date_started | moment }} 
          </p>
          <p>
            Ended: {{ w.date_ended | moment }}
          </p>
        </router-link>
      </li>
    </ul>
  </div>
  <div v-else>
    <p> Nothing to see here. </p>
  </div>
</div>
</template>

<style lang="scss" scoped>
$lgrey : #e2e2e2;

div.latest-workouts {
  padding: 1rem;
}

div.latest-workouts ul li {
  padding: .5rem;
  margin: .5rem 0;
  background: #fff;
}

h3 {
  font-size: 2rem;
  border-bottom: 1px solid $lgrey;
}
</style>

<script>
import api from '../api'
import moment from 'moment'

export default {
  data () {
    return {
      hasLatest: false,
      loading: true,
      error: ''
    }
  },

  computed: {
    latestWorkouts () {
      return this.$store.getters.latestWorkouts
    }
  },

  filters: {
    moment (date) {
      return moment(date).format('MMMM Do YYYY, h:mm:ss a')
    }
  },

  created () {
    // Fetch the latest workouts
    let latest = this.$store.getters.latestWorkouts

    if (!latest.length) {
      console.log('*** created latest workouts')
      api.get('/workouts/').then((res) => {
        this.loading = false
        this.hasLatest = true
        this.$store.dispatch('setLatestWorkouts', { latest: res.body })
      }, (res) => {
        console.log('failed to get data', res)
      })
    } else {
      this.hasLatest = true
    }
  }
}
</script>
