<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <p v-if="formError" class="error">{{ formError }}</p>
      <p class="control has-icon">
        <input class="input text" v-model="username" placeholder="Username" required>
        <i class="fa fa-user"></i>
        <p v-if="usernameError" class="error">{{ usernameError }}</p>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="email" placeholder="Email" required>
        <i class="fa fa-envelope"></i>
        <p v-if="emailError" class="error">{{ emailError }}</p>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="password" placeholder="Password" type="password" required>
        <i class="fa fa-lock"></i>
        <p v-if="passwordError" class="error">{{ passwordError }}</p>
      </p>

      <button class="button is-primary" type="submit">Register</button>
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
  },

  computed: {
    formError () {
      return this.$store.getters.registrationErrors.form
    },
    usernameError () {
      return this.$store.getters.registrationErrors.username
    },
    emailError () {
      return this.$store.getters.registrationErrors.email
    },
    passwordError () {
      return this.$store.getters.registrationErrors.password
    }
  }
}
</script>
