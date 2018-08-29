import "@babel/polyfill";

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";

import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VDivider,
  VToolbar,
  VChip,
  VForm,
  VTextField,
  VExpansionPanel,
  VRadioGroup,
  VProgressCircular,
  transitions
} from "vuetify";
import "vuetify/src/stylus/app.styl";

Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    VDivider,
    VChip,
    VForm,
    VTextField,
    VExpansionPanel,
    VRadioGroup,
    VProgressCircular,
    transitions
  },
  theme: {
    primary: "#06d6a0",
    secondary: "#26547c",
    accent: "#4ce0d2",
    error: "#d62246",
    info: "#26547c",
    success: "#06d6a0",
    warning: "#ffd166"
  }
});

import App from "./App";
import router from "./router";
import Cookies from "js-cookie";

// Apollo
import { ApolloClient } from "apollo-client";
import { createHttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";

import VueApollo from "vue-apollo";

Vue.config.productionTip = false;

const DEBUG = process.env.NODE_ENV === "development";
const API_URL = process.env.VUE_APP_API_URL || "/graphql";

// Apollo setup
const httpLink = createHttpLink({
  uri: API_URL,
  credentials: DEBUG ? "include" : "same-origin",
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
