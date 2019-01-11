<template>
  <v-container>
    <SettingsDataContainer>
      <template slot-scope="slotProps"> 
        <UserSettings :user="slotProps.user" />
      </template>
    </SettingsDataContainer>
  </v-container>
</template>

<script>
import SettingsDataContainer from "@/components/settings/SettingsDataContainer";
import UserSettings from "@/components/settings/UserSettings";

export default {
  name: "SettingsPage",

  components: {
    SettingsDataContainer,
    UserSettings
  }
};
</script>
