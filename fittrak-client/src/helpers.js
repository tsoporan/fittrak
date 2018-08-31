/*
 * Helpers
 */

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

export { getStatusBySlug, statusToSlug };
