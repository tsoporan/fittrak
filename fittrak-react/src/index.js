import React from "react";
import ReactDOM from "react-dom";

import App from "./App";
import * as serviceWorker from "./serviceWorker";

import "./index.css";

ReactDOM.render(<App />, document.getElementById("root"));

/*
 * Offline-first behaviour opt-in
 */
serviceWorker.register();
