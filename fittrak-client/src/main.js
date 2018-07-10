// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import Cookies from "js-cookie";

// Apollo
import { ApolloClient } from "apollo-client";
import { createHttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";

import VueApollo from "vue-apollo";

Vue.config.productionTip = false;

const isDebug = process.env.NODE_ENV !== "production";

// Apollo setup
// TODO: Adapt for production URI
const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql",
  credentials: isDebug ? "include" : "same-origin",
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

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  provide: apolloProvider.provide(),
  components: { App },
  template: "<App/>"
});
