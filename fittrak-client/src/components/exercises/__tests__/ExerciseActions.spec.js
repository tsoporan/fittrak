import { shallowMount } from "@vue/test-utils";

import ExerciseActions from "@/components/exercises/ExerciseActions";

describe("ExerciseActions", () => {
  test("ExerciseActions renders", () => {
    const component = shallowMount(ExerciseActions, {
      propsData: {
        workout: {
          id: 1
        }
      }
    });
    expect(component.html()).toMatchSnapshot();
  });
});
