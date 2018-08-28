import { shallowMount } from "@vue/test-utils";
import Settings from "@/pages/Settings";

describe("Settings", () => {
  test("Settings page renders", () => {
    const app = shallowMount(Settings);
    expect(app.html()).toMatchSnapshot();
  });
});
