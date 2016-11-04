<template>
<div class="latest-workouts">
  <h3> Latest Workouts </h3>
  <div v-if="hasLatest">
    Has latest
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
export default {
  data () {
    return {
      hasLatest: false,
      loading: true
    }
  },
  created () {
    // Fetch the latest workouts
    console.log('*** created latest workouts')
  }
}
</script>
