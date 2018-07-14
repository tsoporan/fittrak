import Vue from "vue";
import Router from "vue-router";

import Home from "@/components/pages/Home.vue";
import WorkoutDetail from "@/components/workouts/WorkoutDetail.vue";
import History from "@/components/pages/History.vue";
import Settings from "@/components/pages/Settings.vue";

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
      path: "/workout/:workoutId",
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
