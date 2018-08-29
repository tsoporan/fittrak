import { shallowMount } from "@vue/test-utils";

import Progress from "@/pages/Progress";

describe("Progress", () => {
  test("Progress page renders", () => {
    const app = shallowMount(Progress);
    expect(app.html()).toMatchSnapshot();
  });
});
