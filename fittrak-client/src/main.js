import Vue from "vue";

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
import "./registerServiceWorker";

import * as Sentry from "@sentry/browser";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

const DEBUG = process.env.NODE_ENV !== "production";
const API_URL = process.env.VUE_APP_API_URL || "/graphql";
const SENTRY_DSN = process.env.VUE_APP_SENTRY_DSN || "";
const SENTRY_ENV = process.env.VUE_APP_SENTRY_ENV || "development";
const SENTRY_RELEASE = process.env.VUE_APP_SENTRY_RELEASE || "";

const MAX_RETRIES = 3;

// Apollo setup

/* Compose multiple links together:
 * - Retry (attempt retries for poor connections)
 * - Error (handle network errors gracefully)
 * - Http (default network request behaviour)
 */
const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors) {
    Sentry.captureException(graphQLErrors);
  }
  if (networkError) {
    Sentry.captureException(networkError);
  }
});

const link = ApolloLink.from([
  new RetryLink({
    delay: {
      initial: 300,
      max: Infinity,
      jitter: true
    },
    attempts: {
      max: MAX_RETRIES,
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
  router,
  apolloProvider,
  components: { App },
  template: "<App/>",
  vuetify
}).$mount("#app");

// Init Sentry
Sentry.init({
  dsn: SENTRY_DSN,
  integrations: [new Sentry.Integrations.Vue({ Vue })],
  environment: SENTRY_ENV,
  release: SENTRY_RELEASE
});
