import { ApolloClient } from "apollo-client";
import { InMemoryCache } from "apollo-cache-inmemory";
import { createHttpLink } from "apollo-link-http";
import { onError } from "apollo-link-error";
import { RetryLink } from "apollo-link-retry";
import { ApolloLink } from "apollo-link";

import Cookies from "js-cookie";

const MAX_RETRIES = 3;

const DEBUG = process.env.NODE_ENV !== "production";

/* Compose multiple links together:
 * - Retry (attempt retries for poor connections)
 * - Error (handle network errors gracefully)
 * - Http (default network request behaviour)
const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors) {
    Sentry.captureException(graphQLErrors);
  }
  if (networkError) {
    Sentry.captureException(networkError);
  }
});
*/

const retryLink = new RetryLink({
  delay: {
    initial: 300,
    max: Infinity,
    jitter: true
  },
  attempts: {
    max: MAX_RETRIES,
    retryIf: (error, _operation) => !!error
  }
});

const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors)
    graphQLErrors.map(({ message, locations, path }) =>
      console.log(
        `[GraphQL error]: Message: ${message}, Location: ${locations}, Path: ${path}`
      )
    );
  if (networkError) console.log(`[Network error]: ${networkError}`);

  // TODO: Sentry
});

const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql",
  credentials: DEBUG ? "include" : "same-origin",
  headers: {
    "x-csrftoken": Cookies.get("csrftoken")
  }
});

const link = ApolloLink.from([retryLink, errorLink, httpLink]);

const client = new ApolloClient({
  link,
  cache: new InMemoryCache(),
  connectToDevTools: !DEBUG
});

export default client;
