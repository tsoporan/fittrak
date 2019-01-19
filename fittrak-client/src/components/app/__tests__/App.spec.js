import { shallowMount } from "@vue/test-utils";

import App from "../App";

describe("App.vue", () => {
  let wrp;

  beforeEach(() => {
    wrp = shallowMount(App, {
      mocks: {
        $apollo: {
          loading: "false"
        }
      }
    });
  });

  it("Renders", () => {
    expect(wrp.html()).toMatchSnapshot();
  });
});
