<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <p class="control has-icon">
        <input class="input text" v-model="username" placeholder="Username" required>
        <i class="fa fa-user"></i>
        <p v-if="errors.username" class="error">{{ errors.username }}</p>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="email" placeholder="Email" required>
        <i class="fa fa-envelope"></i>
        <p v-if="errors.email" class="error">{{ errors.email }}</p>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="password" placeholder="Password" type="password" required>
        <i class="fa fa-lock"></i>
        <p v-if="errors.password" class="error">{{ errors.password }}</p>
      </p>

      <button class="button is-primary" type="submit">Register</button>
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
      username: '',
      email: '',
      password: '',
      errors: {
        username: '',
        email: '',
        password: '',
        formErrors: ''
      }
    }
  },

  methods: {
    register () {
      auth.register(
        this.username,
        this.email,
        this.password
      )
    }
  }
}
</script>
