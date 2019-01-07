<template>
  <v-flex xs12>
    <v-form
      ref="form" 
      v-model="valid"
      lazy-validation
    >

      <v-text-field
        v-model="user.username"
        label="Username"
      />

      <v-text-field
        v-model="user.profile.height"
        label="Height"
        type="number"
      />

      <v-text-field
        v-model="user.profile.weight"
        label="Weight"
        type="number"
      />

      <v-radio-group
        v-model="user.profile.preferredUnit"
        label="Preferred Unit"
      >
        <v-radio 
          label="LBS" 
          value="LBS"/>
        <v-radio 
          label="KGS" 
          value="KGS"/>
      </v-radio-group>

      <v-divider />

      <v-flex text-xs-right>
        <v-btn 
          flat
          outline
        >Submit</v-btn>
      </v-flex>
    </v-form>
  </v-flex>
</template>

<script>
export default {
  name: "UserSettings",

  data: function() {
    return {
      valid: true
    };
  },

  methods: {},

  props: {
    user: {
      type: Object,
      required: true
    }
  }
};
</script>
