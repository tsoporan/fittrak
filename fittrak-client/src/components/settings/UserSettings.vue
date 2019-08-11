<template>
  <v-flex xs12>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field v-model="viewer.username" label="Username" disabled />

      <v-text-field v-model="viewer.email" label="Email" disabled />

      <v-text-field
        v-model="viewer.profile.height"
        label="Height (cm)"
        type="number"
      />

      <v-text-field
        v-model="viewer.profile.weight"
        label="Weight (lbs)"
        type="number"
      />

      <v-radio-group
        v-model="viewer.profile.preferredUnit"
        label="Preferred Workout Unit"
      >
        <v-radio color="primary" label="LBS" value="LBS" />
        <v-radio color="primary" label="KGS" value="KGS" />
      </v-radio-group>
      <v-divider />

      <v-flex text-end mt-4>
        <v-btn rounded dark color="darkGrey" @click.stop="updateSettings"
          >Save</v-btn
        >
      </v-flex>
    </v-form>
  </v-flex>
</template>

<script>
import { mutations } from "@/graphql";

import { showSnackbar } from "@/helpers";

export default {
  name: "UserSettings",

  data() {
    return {
      valid: true
    };
  },

  methods: {
    updateSettings() {
      const { profile } = this.viewer;
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
          mutation: mutations.updateViewerMutation,
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
    viewer: {
      type: Object,
      required: true
    }
  }
};
</script>
