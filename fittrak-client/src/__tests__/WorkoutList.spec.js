import { shallowMount, createLocalVue } from "@vue/test-utils";
import VueRouter from "vue-router";

import WorkoutList from "@/components/workouts/WorkoutList";

describe("WorkoutList.vue", () => {
  const localVue = createLocalVue();
  localVue.use(VueRouter);
  const router = new VueRouter();

  test("WorkoutList renders", () => {
    const component = shallowMount(WorkoutList, {
      localVue,
      router,
      mocks: {
        $apollo: {
          loading: false
        }
      },
      propsData: {
        status: "PENDING",
        title: "Recently",
        limit: 5
      }
    });
    expect(component.html()).toMatchSnapshot();
  });
});
