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

function showSnackbar(type, text, bus = EventBus) {
  bus.$emit("show-snackbar", {
    type,
    text
  });
}

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function getRandomColor() {
  const choices = [
    "red",
    "green",
    "purple",
    "orange",
    "blue",
    "indigo",
    "deep-purple",
    "pink",
    "light-blue",
    "cyan",
    "teal",
    "lime",
    "amber",
    "deep-orange",
    "blue-grey",
    "grey"
  ];

  return pickRandom(choices);
}

export {
  getStatusBySlug,
  statusToSlug,
  showSnackbar,
  EventBus,
  getRandomColor
};
