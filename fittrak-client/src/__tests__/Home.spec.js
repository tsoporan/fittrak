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

    // Set computed
    wrp.vm.now = new Date("2018-08-28");
  });

  it("Renders", () => {
    expect(wrp.html()).toMatchSnapshot();
  });
});
