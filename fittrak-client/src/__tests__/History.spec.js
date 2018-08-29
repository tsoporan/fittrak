import { shallowMount } from "@vue/test-utils";

import History from "@/pages/History";

describe("History", () => {
  test("History page renders", () => {
    const app = shallowMount(History);
    expect(app.html()).toMatchSnapshot();
  });
});
