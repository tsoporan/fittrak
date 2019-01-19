import { shallowMount } from "@vue/test-utils";

import AddSet from "@/components/sets/AddSet";

describe("AddSet.vue", () => {
  test("AddSet renders", () => {
    const component = shallowMount(AddSet, {
      propsData: {
        exercise: {
          id: 1
        }
      }
    });
    expect(component.html()).toMatchSnapshot();
  });
});
