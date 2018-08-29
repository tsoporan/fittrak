import { shallowMount } from "@vue/test-utils";

import AddSet from "../components/sets/AddSet";

describe("AddSet.vue", () => {
  test("AddSet renders", () => {
    const component = shallowMount(AddSet);
    expect(component.html()).toMatchSnapshot();
  });
});
