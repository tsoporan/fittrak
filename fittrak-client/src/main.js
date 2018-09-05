import "@babel/polyfill";

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";

import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VMenu,
  VFooter,
  VList,
  VBtn,
  VBtnToggle,
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
  VCard,
  VAutocomplete,
  transitions
} from "vuetify";
import "vuetify/src/stylus/app.styl";

Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VMenu,
    VFooter,
    VList,
    VBtn,
    VBtnToggle,
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
    VCard,
    VAutocomplete,
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
import { ApolloLink } from "apollo-link";
import { RetryLink } from "apollo-link-retry";
import { HttpLink } from "apollo-link-http";
import { onError } from "apollo-link-error";
import { InMemoryCache } from "apollo-cache-inmemory";

import VueApollo from "vue-apollo";

Vue.config.productionTip = false;

const DEBUG = process.env.NODE_ENV === "development";
const API_URL = process.env.VUE_APP_API_URL || "/graphql";

// Apollo setup

/* Compose multiple links together:
 * - Retry (attempt retries for poor connections)
 * - Error (handle network errors gracefully)
 * - Http (default network request behaviour)
 */
const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors)
    graphQLErrors.map(({ message, locations, path }) =>
      // eslint-disable-next-line
      console.log(
        `[GraphQL error]: Message: ${message}, Location: ${locations}, Path: ${path}`
      )
    );
  // eslint-disable-next-line
  if (networkError) console.log(`[Network error]: ${networkError}`);
});

const link = ApolloLink.from([
  new RetryLink({
    delay: {
      initial: 300,
      max: Infinity,
      jitter: true
    },
    attempts: {
      max: 5,
      retryIf: error => !!error
    }
  }),
  errorLink,
  new HttpLink({
    uri: API_URL,
    credentials: DEBUG ? "include" : "same-origin",
    headers: {
      "x-csrftoken": Cookies.get("csrftoken")
    }
  })
]);

const apolloClient = new ApolloClient({
  link,
  cache: new InMemoryCache(),
  connectToDevTools: !DEBUG
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
