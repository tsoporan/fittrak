<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <label>
        <input class="input text" v-model="email" placeholder="Email" required>
        <p v-if="errors.username" class="error">{{ errors.username }}</p>
      </label>
      <label>
        <input class="input text" v-model="password" placeholder="Password" type="password" required>
        <p v-if="errors.password" class="error">{{ errors.password }}</p>
      </label>
      <button class="button" type="submit">login</button>
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

