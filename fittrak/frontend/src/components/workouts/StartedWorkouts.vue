<template>
<div class="started-workouts">
  <h3> Started Workouts </h3>

  <div v-if="hasStarted">
      Has started.
  </div>
  <div v-else>
    <p> Nothing to see here. </p>
  </div>

</div>
</template>

<style lang="scss" scoped>
$lgrey : #e2e2e2;

div.started-workouts {
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
      hasStarted: false,
      loading: true
    }
  },
  created () {
    // Fetch started workouts
    console.log('*** created started workouts')
  }
}
</script>
