/*
 * Helpers
 */

import Vue from "vue";

import {
  STATUS_MAP,
  PENDING,
  CANCELLED,
  COMPLETE,
  PAUSED,
  IN_PROGRESS
} from "@/constants";

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

function showSnackbar(type, text, sticky = false, bus = EventBus) {
  bus.$emit("show-snackbar", {
    type,
    text,
    sticky
  });
}

function getStatusColor(status) {
  const statusMap = {
    [PENDING]: "blue-grey",
    [IN_PROGRESS]: "blue",
    [COMPLETE]: "green",
    [CANCELLED]: "red",
    [PAUSED]: "grey"
  };

  return statusMap[status];
}

export {
  getStatusBySlug,
  statusToSlug,
  showSnackbar,
  EventBus,
  getStatusColor
};
