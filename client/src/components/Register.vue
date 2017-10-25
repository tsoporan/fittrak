<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <p v-if="formErrors" v-for="e in formErrors" class="help is-danger">{{ e }}</p>

      <div class="field">
        <div class="control has-icons-left has-icons-right">
          <input class="input" v-model="username" v-bind:class="{ 'is-danger': usernameErrors }" type="text" placeholder="Your username" value="">
          <span class="icon is-small is-left">
            <i class="fa fa-user"></i>
          </span>
        </div>
        <span v-if="usernameErrors">
          <p v-for="e in usernameErrors" class="help is-danger">{{ e }}</p>
        </span>
      </div>

      <div class="field">
        <div class="control has-icons-left has-icons-right">
          <input class="input" v-model="email" v-bind:class="{ 'is-danger': emailErrors}" type="email" placeholder="Your email" value="">
          <span class="icon is-small is-left">
            <i class="fa fa-envelope"></i>
          </span>
        </div>
        <span v-if="emailErrors">
          <p v-for="e in emailErrors" class="help is-danger">{{ e }}</p>
        </span>
      </div>

      <div class="field">
        <div class="control has-icons-left has-icons-right">
          <input class="input" v-model="password" v-bind:class="{ 'is-danger': passwordErrors}" type="password" placeholder="Your password" value="">
          <span class="icon is-small is-left">
            <i class="fa fa-lock"></i>
          </span>
        </div>
        <span v-if="passwordErrors">
          <p v-for="e in passwordErrors" class="help is-danger">{{ e }}</p>
        </span>
      </div>



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
      passwordErrors: null,
      usernamErrors: null,
      emailErrors: null,
      formErrors: null
    }
  },

  methods: {
    register () {
      auth.register(
        this.username,
        this.email,
        this.password
      ).catch(r => {
        this.passwordErrors = r.body.password
        this.usernameErrors = r.body.username
        this.emailerrors = r.body.email
        this.formErrors = r.body.non_field_errors
      })
    }
  }
}
</script>
