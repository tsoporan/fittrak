import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NewWorkout from "./views/NewWorkout.vue";
import History from "./views/History.vue";
import Settings from "./views/Settings.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/history",
      name: "history",
      component: History
    },
    {
      path: "/settings",
      name: "settings",
      component: Settings
    },
    {
      path: "/new",
      name: "new-workout",
      component: NewWorkout
    }
  ]
});
