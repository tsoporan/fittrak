import { shallowMount } from "@vue/test-utils";
import SetItem from "../components/sets/SetItem";

describe("SetItem.vue", () => {
  test("SetItem renders", () => {
    const component = shallowMount(SetItem, {
      propsData: {
        set: {
          id: 1,
          weight: 1,
          reps: 1
        }
      }
    });
    expect(component.html()).toMatchSnapshot();
  });
});
