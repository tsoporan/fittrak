from typing import Any, Dict, List, Optional

from .models import WorkoutEvent

# TODO: Rework this, need a more powerful templating language? Jinja?
action_template: dict = {
    "create_workout": 'New workout created at "{state[created_at]}"',
    "update_workout": 'Workout "{state[current[slug]]}" has been updated with: "{state[changed]}"',
    "remove_workout": 'Workout "{state[slug]}" has been removed',
}


def clean_models(models: List) -> List[Dict]:
    """
    Turns a model into a dict stripping away 'unwanted' fields
    i.e fields starting with an underscore
    """

    cleaned = []

    for model in models:
        fields = vars(model)

        cleaned.append(
            {key: value for key, value in fields.items() if not key.startswith("_")}
        )

    return cleaned


def create_workout_event(
    *, workout, action: str, user, state: Optional[Dict[str, Any]] = None
) -> None:
    # Use the current model as state by default,
    # otherwise favour the new state passed in - useful for
    # updated fields.

    if not state:
        state = clean_models([workout])
    else:
        # Custom state should be "dictized", however
        # values can be arrays

        for k, v in state.items():
            if isinstance(v, list):
                state[k] = clean_models(v)
            else:
                state[k] = clean_models([v])

    WorkoutEvent.objects.create(workout=workout, action=action, user=user, state=state)
