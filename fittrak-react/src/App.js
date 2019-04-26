import React from "react";
import { ApolloProvider } from "react-apollo";
import { Router } from "@reach/router";

import CssBaseline from "@material-ui/core/CssBaseline";
import { MuiThemeProvider, createMuiTheme } from "@material-ui/core/styles";

import client from "./config";

import Landing from "./pages/Landing";

const theme = createMuiTheme({
  typography: {
    useNextVariants: true // Sup[port typo v2
  }
});

const App = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <ApolloProvider client={client}>
        <MuiThemeProvider theme={theme}>
          <Router>
            <Landing path="/" />
          </Router>
        </MuiThemeProvider>
      </ApolloProvider>
    </React.Fragment>
  );
};

export default App;
