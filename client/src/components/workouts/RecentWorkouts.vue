<template>
<v-flex>
  <v-list 
    v-if="latestWorkouts.length"
    two-lines
  >
    <template v-for="(workout, index) in latestWorkouts"> 
      <v-list-tile
        :key="workout.id"
        @click=""
      >
        <v-list-tile-content>
          <v-list-tile-title>Workout {{ index }}</v-list-tile-title>
          <v-list-tile-sub-title class="grey--text text--darken-4">{{ workout.started | formatDate }}</v-list-tile-sub-title>
        </v-list-tile-content>

      </v-list-tile>
      <v-divider v-if="index + 1 < latestWorkouts.length" :key="workout.id"></v-divider>
    </template>
  </v-list>
  <h5 v-else>You currently have no workout history, start a workout first!</h5>

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

export default {
  data: () => ({
    fetching: false,
    error: ''
  }),

  filters: {
    formatDate: function (value) {
      return moment(value).format('HH:MM on YYYY-MM-DD')
    }
  },

  computed: {
    ...mapState({
      latestWorkouts: state => state.workouts.latest
    })
  }
}
</script>
