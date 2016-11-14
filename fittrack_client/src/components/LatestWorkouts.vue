<template>
<div class="latest-workouts">
  <h3> Latest Workouts </h3>
  <div v-if="hasLatest">
    <ul>
      <li v-for="w in latestWorkouts">
        Workout {{ w.date_started }} - {{ w.date_ended }}
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

h3 {
  font-size: 2rem;
  border-bottom: 1px solid $lgrey;
}
</style>

<script>
import utils from '../utils'

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
      return this.$store.state.workouts.latest
    }
  },

  created () {
    // Fetch the latest workouts
    let latest = this.$store.state.workouts.latest

    if (!latest.length) {
      console.log('*** created latest workouts')
      utils.getData('/workouts/').then((res) => {
        this.loading = false
        this.hasLatest = true
        this.$store.commit('setLatestWorkouts', { latest: res.body })
      }, (res) => {
        console.log('failed to get data', res)
      })
    } else {
      this.hasLatest = true
    }
  }
}
</script>
