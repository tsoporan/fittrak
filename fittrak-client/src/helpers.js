/*
 * Helpers
 */

import Vue from "vue";

import { STATUS_MAP } from "@/constants";

function getStatusBySlug(slug) {
  const statusKey = slug.toUpperCase().replace("-", "_");

  if (Object.keys(STATUS_MAP).includes(statusKey)) {
    return statusKey;
  }

  return null;
}

function statusToSlug(name) {
  return name.toLowerCase().replace(" ", "-");
}

// Vue instance used as a global event bus
const EventBus = new Vue();

export { getStatusBySlug, statusToSlug, EventBus };
