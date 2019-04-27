import React from "react";
import { ApolloProvider, Query } from "react-apollo";
import { Router } from "@reach/router";

import CssBaseline from "@material-ui/core/CssBaseline";
import { MuiThemeProvider, createMuiTheme } from "@material-ui/core/styles";

import client from "./config";

import Landing from "./pages/Landing";
import NewWorkout from "./pages/NewWorkout";

import queries from "./graphql/queries";

import AuthContext from "./context";

const theme = createMuiTheme({
  typography: {
    useNextVariants: true // Sup[port typo v2
  },
  palette: {
    primary: { main: "#03A9F4", contrastText: "#F5F5F5" },
    secondary: { main: "#37474F" }
  }
});

const App = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <ApolloProvider client={client}>
        <MuiThemeProvider theme={theme}>
          <Query query={queries.viewerQuery}>
            {({ loading, error, data }) => {
              if (loading) return "Loading";
              if (error) return "Error";

              return (
                <AuthContext.Provider value={data.viewer}>
                  <Router>
                    <Landing path="/" />
                    <NewWorkout path="/new-workout" />
                  </Router>
                </AuthContext.Provider>
              );
            }}
          </Query>
        </MuiThemeProvider>
      </ApolloProvider>
    </React.Fragment>
  );
};

export default App;
