<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <p class="control has-icon">
        <input class="input text" v-model="email" placeholder="Email" required>
        <i class="fa fa-envelope"></i>
        <p v-if="errors.username" class="error">{{ errors.username }}</p>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="password" placeholder="Password" type="password" required>
        <i class="fa fa-lock"></i>
        <p v-if="errors.password" class="error">{{ errors.password }}</p>
      </p>

      <button class="button is-primary" type="submit">Login</button>
      <p v-if="errors.formErrors" class="error">{{ errors.formErrors }}</p>
    </form>
  </div>
</template>

<style lang="scss" scoped>
</style>

<script>
import auth from '../auth'

export default {
  data () {
    return {
      email: '',
      password: '',
      errors: {
        username: '',
        password: '',
        formErrors: ''
      }
    }
  },

  methods: {
    login () {
      auth.login(
        this.email,
        this.password,
        this
      )
    }
  }
}
</script>

