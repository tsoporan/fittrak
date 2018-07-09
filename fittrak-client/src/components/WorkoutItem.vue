<template>
  <li>
    ID: {{ workout.id }}
    Started: {{ workout.dateStarted }}
    Ended: {{ workout.dateEnded }}
    Status: {{ getHumanStatus }}
    <h3>Exercises: {{ exercises.length }}</h3>
  </li>
</template>

<script>
const STATUS_MAP = {
  IN_PROGRESS: "In Progress",
  CANCELLED: "Cancelled",
  COMPLETE: "Complete"
};

export default {
  name: "WorkoutItem",
  computed: {
    // Human friendly status
    getHumanStatus: data => {
      return STATUS_MAP[data.workout.status];
    },
    exercises: data => {
      return data.workout.exercises;
    }
  },
  props: {
    workout: Object
  }
};
</script>
