import { shallowMount } from "@vue/test-utils";

import Home from "@/pages/Home";

describe("Home", () => {
  test("Home page renders", () => {
    const app = shallowMount(Home);
    expect(app.html()).toMatchSnapshot();
  });
});
