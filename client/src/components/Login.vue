<template>
<v-flex xs6>
  <h2>Login</h2>
  <v-form v-model="valid" ref="form" lazy-validation>
    <v-text-field
      label="Your email"
      v-model="email"
      type="email"
      :rules="emailRules"
    >
    </v-text-field>
    <v-text-field
      label="Your password"
      v-model="password"
      type="password"
      :rules="passwordRules"
      >
    </v-text-field>
    <v-btn 
      @click.submit=""
      color="cyan lighten-1"
      dark
      >Submit
    </v-btn>
  </v-form>
</v-flex>
</template>

<script>
import auth from '../auth'

export default {
  data: () => ({
    valid: true,
    email: '',
    password: '',
    emailRules: [
      (v) => !!v || 'Email is required'
    ],
    passwordRules: [
      (v) => !!v || 'Password is required'
    ]
  }),

  methods: {
    login () {
      auth.login(
        this.email,
        this.password
      ).catch(r => {
        this.passwordErrors = r.body.password
        this.usernameErrors = r.body.username
        this.formErrors = r.body.non_field_errors
      })
    }
  }
}
</script>

