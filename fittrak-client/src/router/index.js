import Vue from "vue";
import Router from "vue-router";

import Home from "@/components/Home.vue";
import WorkoutDetail from "@/components/WorkoutDetail.vue";
import History from "@/components/History.vue";
import Settings from "@/components/Settings.vue";

Vue.use(Router);

export default new Router({
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
