/*
 * Constants
 */

const PENDING = "PENDING";
const IN_PROGRESS = "IN_PROGRESS";
const CANCELLED = "CANCELLED";
const COMPLETE = "COMPLETE";

const STATUS_MAP = Object.freeze({
  [PENDING]: "Pending",
  [IN_PROGRESS]: "In Progress",
  [CANCELLED]: "Cancelled",
  [COMPLETE]: "Complete"
});

export { STATUS_MAP, PENDING, IN_PROGRESS, CANCELLED, COMPLETE };
