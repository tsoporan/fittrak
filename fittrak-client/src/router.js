import Vue from "vue";
import Router from "vue-router";

import Home from "@/pages/Home.vue";
import WorkoutDetail from "@/pages/WorkoutDetail.vue";
import History from "@/pages/History.vue";
import Settings from "@/pages/Settings.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/workouts/:workoutId",
      name: "WorkoutDetail",
      component: WorkoutDetail
    },
    {
      path: "/history",
      name: "History",
      component: History
    },
    {
      path: "/settings",
      name: "Settings",
      component: Settings
    }
  ]
});
