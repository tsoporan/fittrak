<template>
  <v-toolbar flat dense color="grey lighten-5" class="mt-3 mb-3">
    <v-toolbar-title>Viewing: {{ selectedStatus || "All" }}</v-toolbar-title>
    <v-spacer />
    <v-toolbar-items>
      <v-menu close-on-click bottom>
        <v-flex xs2 slot="activator">
          <v-btn depressed color="secondary" small>By Status</v-btn>
        </v-flex>
        <v-list>
          <v-list-tile
            v-for="(status, idx) in statuses" 
            :key="idx"
            flat
            color="secondary"
            @click.stop="changeStatus(idx, status)"
          >
          {{ status }}
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import { STATUS_MAP } from "@/constants";
import { statusToSlug } from "@/helpers";

export default {
  name: "WorkoutHistoryToolbar",
  data() {
    return {
      statuses: [
        STATUS_MAP.IN_PROGRESS,
        STATUS_MAP.PENDING,
        STATUS_MAP.COMPLETE,
        STATUS_MAP.CANCELLED
      ],
      selectedStatus: null
    };
  },

  methods: {
    changeStatus(currentIdx, status) {
      const slug = statusToSlug(status);

      this.selectedStatus = status;
      this.$router.push(`/history/${slug}`);
    }
  }
};
</script>
