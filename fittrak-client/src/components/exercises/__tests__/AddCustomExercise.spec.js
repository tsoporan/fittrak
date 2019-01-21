import { shallowMount } from "@vue/test-utils";

import AddCustomExercise from "@/components/exercises/AddCustomExercise";

describe("AddCustomExercise", () => {
  test("AddCustomExercise renders", () => {
    const component = shallowMount(AddCustomExercise, {
      propsData: {
        workout: {
          id: 1
        }
      }
    });
    expect(component.html()).toMatchSnapshot();
  });
});
