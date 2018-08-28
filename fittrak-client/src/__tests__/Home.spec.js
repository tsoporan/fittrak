import { shallowMount } from "@vue/test-utils";

import Home from "@/pages/Home";

describe("Home", () => {
  let wrp;

  beforeEach(() => {
    wrp = shallowMount(Home, {
      mocks: {
        $vuetify: {
          breakpoint: "xs"
        }
      }
    });
  });

  it("Renders", () => {
    expect(wrp.html()).toMatchSnapshot();
  });
});
