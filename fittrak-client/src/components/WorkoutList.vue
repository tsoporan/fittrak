<template>
  <div>
    <h2>{{ title }}</h2>
    <p v-if="workouts.length">
      Workouts
      <ul>
        <WorkoutItem
         v-for="workout in workouts" 
          :key="workout.id"
          :workout="workout"
          />
      </ul>
    </p>
    <p v-else>
      No workouts!
    </p>
  </div>
</template>

<script>
import gql from "graphql-tag";
import WorkoutItem from "./WorkoutItem";

export default {
  name: "WorkoutList",

  data() {
    return {
      workouts: []
    };
  },

  apollo: {
    workouts: {
      query() {
        return gql`
          {
            viewer {
              workouts {
                id
                dateStarted
                dateEnded
                isActive
                status
                slug
                exercises {
                  id
                }
              }
            }
          }
        `;
      },

      update: data => data.viewer.workouts
    }
  },

  components: {
    WorkoutItem
  },

  props: {
    title: String
  }
};
</script>
