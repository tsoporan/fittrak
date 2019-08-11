module.exports = {
  root: true,

  env: {
    node: true,
    jest: true
  },

  rules: {
    "no-console": "off",
    "no-debugger": "off"
  },

  parserOptions: {
    parser: "babel-eslint"
  },

  extends: ["plugin:vue/strongly-recommended", "@vue/prettier"]
};
