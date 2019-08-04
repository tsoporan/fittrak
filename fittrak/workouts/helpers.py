import datetime
from typing import Dict, Optional

from .models import WorkoutEvent

action_template: dict = {
    "create_workout": 'New workout created at "{state[created_at]}"',
    "update_workout": 'Workout "{state[current[slug]]}" has been updated with: "{state[changed]}"',
    "remove_workout": 'Workout "{state[slug]}" has been removed',
}


def merge_dicts(*dicts) -> dict:
    result: dict = {}

    for d in dicts:
        result.update(d)

    return result


def model_as_dict(model) -> dict:
    """
    Turns a model into a dict stripping away 'unwanted' fields, i.e start
    with an underscore
    """
    fields = vars(model)

    return {key: value for key, value in fields.items() if not key.startswith("_")}


def serialize_state(state):
    for k, v in state.items():
        if isinstance(v, datetime.datetime):
            state[k] = v.strftime("%Y-%m-%d %H:%M")

    return state


def create_workout_event(
    *, workout, action: str, user, state: Optional[Dict] = None
) -> None:
    try:
        template = action_template[action]
    except KeyError:
        # TODO: Logging
        pass

    # Use the current model as state by default,
    # otherwise favour the new state passed in - useful for
    # updated fields.

    if not state:
        state = model_as_dict(workout)

    message = template.format(state=serialize_state(state))

    WorkoutEvent.objects.create(
        workout=workout, action=action, user=user, state=state, message=message
    )
