import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import Cookies from "js-cookie";

// Apollo
import { ApolloClient } from "apollo-client";
import { createHttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";

import VueApollo from "vue-apollo";

Vue.config.productionTip = false;

// Apollo setup
// TODO: Adapt for production URI
const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql",
  credentials: "include", // TODO: same-origin for prod
  headers: {
    "x-csrftoken": Cookies.get("csrftoken")
  }
});

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
});

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

Vue.use(VueApollo);

new Vue({
  router,
  store,
  provide: apolloProvider.provide(),
  render: h => h(App)
}).$mount("#app");
