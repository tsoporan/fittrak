<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <p v-if="formError" class="error">{{ formError }}</p>
      <p class="control has-icon">
        <input class="input text" v-model="email" placeholder="Email" required>
        <i class="fa fa-envelope"></i>
        <p v-if="usernameError" class="error">{{ usernameError }}</p>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="password" placeholder="Password" type="password" required>
        <i class="fa fa-lock"></i>
        <p v-if="passwordError" class="error">{{ passwordError }}</p>
      </p>

      <button class="button is-primary" type="submit">Login</button>
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
      password: ''
    }
  },

  methods: {
    login () {
      auth.login(
        this.email,
        this.password
      )
    }
  },

  computed: {
    formError () {
      return this.$store.getters.loginErrors.form
    },
    usernameError () {
      return this.$store.getters.loginErrors.username
    },
    passwordError () {
      return this.$store.getters.loginErrors.password
    }
  }
}
</script>

