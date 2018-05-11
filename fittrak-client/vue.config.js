const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  lintOnSave: false,
  baseUrl: '/static/',
  outputDir: "../fittrak/assets/bundles",
  configureWebpack: {
    plugins: [
      new BundleTracker({filename: "../fittrak/webpack-stats.json"}),
    ]
  }
};
