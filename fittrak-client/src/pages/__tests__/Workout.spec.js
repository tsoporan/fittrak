import { shallowMount } from "@vue/test-utils";

import Workout from "@/pages/Workout";

describe("Workout", () => {
  test("Workout page renders", () => {
    const app = shallowMount(Workout);
    expect(app.html()).toMatchSnapshot();
  });
});
