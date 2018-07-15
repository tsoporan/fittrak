// Constants

const IN_PROGRESS = "IN_PROGRESS";
const CANCELLED = "CANCELLED";
const COMPLETE = "COMPLETE";

const STATUS_MAP = Object.freeze({
  [IN_PROGRESS]: "In Progress",
  [CANCELLED]: "Cancelled",
  [COMPLETE]: "Complete"
});

export { STATUS_MAP, IN_PROGRESS, CANCELLED, COMPLETE };
