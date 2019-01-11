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
        disabled
      />

      <v-text-field
        v-model="user.email"
        label="Email"
        disabled
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

      <v-flex 
        text-xs-right 
        mt-3>
        <v-btn 
          flat
          outline
          @click.stop="updateSettings"
        >Save</v-btn>
      </v-flex>
    </v-form>
  </v-flex>
</template>

<script>
import UpdateSettingsMutation from "@/graphql/mutations/updateSettings.graphql";

import { showSnackbar } from "@/helpers";

export default {
  name: "UserSettings",

  data: function() {
    return {
      valid: true
    };
  },

  methods: {
    updateSettings() {
      const { profile } = this.user;
      let { height, weight, preferredUnit } = profile;

      // Should be treating these as null
      if (height === "") {
        height = null;
      }

      if (weight === "") {
        weight = null;
      }

      this.$apollo
        .mutate({
          mutation: UpdateSettingsMutation,
          variables: {
            height,
            weight,
            preferredUnit
          }
        })
        .then(() => {
          showSnackbar("success", "Settings saved.");
        })
        .catch(() => {
          showSnackbar("error", "Could not save settings.");
        });
    }
  },

  props: {
    user: {
      type: Object,
      required: true
    }
  }
};
</script>
