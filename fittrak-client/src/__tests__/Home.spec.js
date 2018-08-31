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
      dayName: "Monday",
      dayNum: "8th",
      dayTime: "8:00PM"
    };
  });

  it("Renders", () => {
    expect(wrp.html()).toMatchSnapshot();
  });
});
