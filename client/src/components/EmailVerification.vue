<template>
  <div>
    <h2>Email Verification</h2>
  </div>
</template>

<style lang="scss" scoped>
</style>

<script>
import auth from '../auth'

export default {
  created () {
    auth.emailVerification(this.$route.query.key)
  }
}
</script>
