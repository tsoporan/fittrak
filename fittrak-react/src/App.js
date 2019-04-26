import React from "react";

import { ApolloProvider } from "react-apollo";
import { Router } from "@reach/router";
import CssBaseline from "@material-ui/core/CssBaseline";

import client from "./config";

import Landing from "./pages/Landing";

const App = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <ApolloProvider client={client}>
        <Router>
          <Landing path="/" />
        </Router>
      </ApolloProvider>
    </React.Fragment>
  );
};

export default App;
