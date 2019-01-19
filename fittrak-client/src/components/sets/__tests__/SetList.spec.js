import { shallowMount } from "@vue/test-utils";

import SetList from "@/components/sets/SetList";

describe("SetList.vue", () => {
  test("SetList renders", () => {
    const component = shallowMount(SetList, {
      propsData: {
        sets: [
          {
            id: 1,
            repetitions: 10,
            weight: 100,
            unit: "LB"
          }
        ],
        exercise: {
          id: 1
        }
      }
    });
    expect(component.html()).toMatchSnapshot();
  });
});
