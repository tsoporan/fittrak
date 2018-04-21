<template>
<v-flex class="xs12 text-xs-center">

  <template v-if="fetching">
    <v-progress-circular 
      color="cyan"
      indeterminate 
      size=48
    >
    </v-progress-circular>
  </template>

  <template v-else>
  <h2>Recently</h2>
  <v-list 
    v-if="recentWorkouts.length"
    style="padding: 0"
  >
    <template v-for="(workout, index) in recentWorkouts"> 
      <v-list-tile
        :key="workout.id"
        @click=""
      >
          <p>{{ workout.started | asDay  }}</p>
          <p>Started: {{ workout.started | formatDate }}, Ended: {{ workout.ended | formatDate }}</p>
          <p>Total Exercises: {{ workout.exercises.length }}</p>
          <p>Status: {{ workout.status.name }}</p>
      </v-list-tile>
      <v-divider v-if="index + 1 < recentWorkouts.length" :key="workout.id"></v-divider>
    </template>
  </v-list>
  <h5 v-else>You currently have no workout history, start a workout first!</h5>
  </template>

  <v-snackbar 
    v-model="error"
    color="red"
  >
    {{ error }}
  </v-snackbar>

</v-flex>
</template>

<script>
import { mapState } from 'vuex'
import moment from 'moment'
import api from '../../api'

export default {
  data: () => ({
    fetching: false,
    error: ''
  }),

  filters: {
    formatDate: function (value) {
      return moment(value).format('HH:MM,  YYYY-MM-DD')
    },
    asDay: function (value) {
      return moment(value).format('dddd Do')
    }

  },

  computed: {
    ...mapState({
      recentWorkouts: state => state.workouts.recent
    })
  },

  mounted: function () {
    this.fetching = true

    return api.getRecentWorkouts().then((res) => {
      this.fetching = false
      this.$store.dispatch('setRecentWorkouts', {
        workouts: res.body
      })
    }).catch((err) => {
      this.fetching = false
      this.err = err
    })
  }
}
</script>
