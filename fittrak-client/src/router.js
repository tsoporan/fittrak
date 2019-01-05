import Vue from "vue";
import Router from "vue-router";

import HomePage from "@/pages/Home.vue";
import WorkoutPage from "@/pages/Workout.vue";
import HistoryPage from "@/pages/History.vue";
import SettingsPage from "@/pages/Settings.vue";
import ProgressPage from "@/pages/Progress.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "FitTrak",
      component: HomePage
    },
    {
      path: "/workouts/:workoutId",
      name: "Workout",
      component: WorkoutPage
    },
    {
      path: "/history/:status?",
      name: "History",
      component: HistoryPage
    },
    {
      path: "/settings",
      name: "Settings",
      component: SettingsPage
    },
    {
      path: "/progress",
      name: "Progress",
      component: ProgressPage
    }
  ]
});
