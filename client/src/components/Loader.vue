<template>
<v-layout justify-center align-center>
  <v-progress-circular 
    color="cyan"
    indeterminate 
    size=128
  >
  </v-progress-circular>
</v-layout>
</template>

<script>

export default {
  mounted: function () {
    // Fresh data from the API
    // For now we'll mock this with a setTimeout
    setTimeout(() => {
      this.$store.dispatch('refreshData', {
        meta: {}
      })
    }, 1500)
  }
}
</script>
