import { shallowMount } from "@vue/test-utils";
import Settings from "@/pages/Settings";

describe("Settings", () => {
  test("Settings page renders", () => {
    const app = shallowMount(Settings, {
      propsData: {
        viewer: {
          username: "foo",
          email: "foo@baz.com"
        }
      }
    });

    expect(app.html()).toMatchSnapshot();
  });
});
