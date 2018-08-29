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
    wrp.vm.now = {
      dayPart: "Monday",
      numPart: "8th",
      hourMin: "8:00PM"
    };
  });

  it("Renders", () => {
    expect(wrp.html()).toMatchSnapshot();
  });
});
