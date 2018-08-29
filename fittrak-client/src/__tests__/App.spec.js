import { shallowMount } from "@vue/test-utils";

import App from "../App";

describe("App.vue", () => {
  test("App renders", () => {
    const app = shallowMount(App);
    expect(app.html()).toMatchSnapshot();
  });
});
