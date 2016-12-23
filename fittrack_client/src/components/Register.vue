<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <p v-if="formError" class="error">{{ formError }}</p>
      <p class="control has-icon">
        <input class="input text" v-model="username" placeholder="Username" required>
        <i class="fa fa-user"></i>
        <ul>
          <li v-for="error in usernameErrors">
            {{ error }}
          </li>
        </ul>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="email" placeholder="Email" required>
        <i class="fa fa-envelope"></i>
        <ul>
          <li v-for="error in emailErrors">
            {{ error }}
          </li>
        </ul>
      </p>
      <p class="control has-icon">
        <input class="input text" v-model="password" placeholder="Password" type="password" required>
        <i class="fa fa-lock"></i>
        <ul>
          <li v-for="error in passwordErrors">
            {{ error }}
          </li>
        </ul>
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
    usernameErrors () {
      return this.$store.getters.registrationErrors.username
    },
    emailErrors () {
      return this.$store.getters.registrationErrors.email
    },
    passwordErrors () {
      return this.$store.getters.registrationErrors.password
    }
  }
}
</script>
