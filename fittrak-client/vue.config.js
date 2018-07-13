// FitTrak Vue Config

const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  baseUrl: "/static/",
  outputDir: "../fittrak/assets/bundles",
  configureWebpack: {
    plugins: [new BundleTracker({ filename: "../fittrak/webpack-stats.json" })],
    resolve: {
      alias: {
        vue$: "vue/dist/vue.esm.js"
      }
    }
  },
  chainWebpack: config => {
    // GraphQL Loader
    config.module
      .rule("graphql")
      .test(/\.(gql|graphql)$/)
      .use("graphql-tag/loader")
      .loader("graphql-tag/loader")
      .end();
  }
};
