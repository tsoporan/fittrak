/*
 * Constants
 */

const APP_NAME = "FitTrak";

const PENDING = "PENDING";
const IN_PROGRESS = "IN_PROGRESS";
const CANCELLED = "CANCELLED";
const COMPLETE = "COMPLETE";
const ARCHIVED = "ARCHIVED";
const PAUSED = "PAUSED";

const STATUS_MAP = Object.freeze({
  [PENDING]: "Pending",
  [IN_PROGRESS]: "In Progress",
  [CANCELLED]: "Cancelled",
  [COMPLETE]: "Complete",
  [ARCHIVED]: "Archived",
  [PAUSED]: "Paused"
});

// List limit
const DEFAULT_LIMIT = 5;

// This is a server-side handled logout
const SIGNOUT_URL = "/accounts/logout/";

export {
  STATUS_MAP,
  PENDING,
  IN_PROGRESS,
  CANCELLED,
  COMPLETE,
  ARCHIVED,
  PAUSED,
  DEFAULT_LIMIT,
  SIGNOUT_URL,
  APP_NAME
};
