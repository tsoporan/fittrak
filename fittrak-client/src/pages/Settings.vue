<template>
  <v-container>
    <SettingsDataContainer>
      <template slot-scope="slotProps">
        <v-flex xs12>
          {{ slotProps.settings.id }}
          {{ slotProps.settings.username }}
        </v-flex>
      </template>
    </SettingsDataContainer>
  </v-container>
</template>

<script>
import SettingsDataContainer from "@/components/settings/SettingsDataContainer";

export default {
  name: "SettingsPage",

  components: {
    SettingsDataContainer
  }
};
</script>
