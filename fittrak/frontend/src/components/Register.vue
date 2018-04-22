<template>
<v-layout justify-center align-center>
<v-flex class="xs10">
  <h2 class="text-xs-center">Register</h2>
  <v-form v-model="valid" ref="form" lazy-validation>
    <v-text-field
      label="Your email"
      v-model="email"
      type="email"
      :rules="emailRules"
    >
    </v-text-field>
    <v-text-field
      label="New password"
      v-model="password"
      type="password"
      :rules="passwordRules"
      >
    </v-text-field>
    <v-btn 
      @click.submit="register"
      color="cyan lighten-1"
      dark
      >Register
    </v-btn>
  </v-form>
</v-flex>
</v-layout>
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
    register () {
      auth.register(
        this.email, // Username same as email
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
