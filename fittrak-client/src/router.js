import Vue from "vue";
import Router from "vue-router";

import Home from "@/pages/Home.vue";
import WorkoutDetail from "@/pages/WorkoutDetail.vue";
import WorkoutSetup from "@/pages/WorkoutSetup.vue";
import History from "@/pages/History.vue";
import Settings from "@/pages/Settings.vue";
import Progress from "@/pages/Progress.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "FitTrak",
      component: Home
    },
    {
      path: "/workouts/:workoutId/detail",
      name: "WorkoutDetail",
      component: WorkoutDetail
    },
    {
      path: "/workouts/:workoutId/setup",
      name: "WorkoutSetup",
      component: WorkoutSetup
    },
    {
      path: "/history/:status?",
      name: "History",
      component: History
    },
    {
      path: "/settings",
      name: "Settings",
      component: Settings
    },
    {
      path: "/progress",
      name: "Progress",
      component: Progress
    }
  ]
});
