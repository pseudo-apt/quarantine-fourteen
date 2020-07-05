import copy
from typing import Callable, Dict, List, Optional, Tuple


class Action:
    """
    Generic action class for updating the game state.
    """

    def __init__(self, fn: Callable[["QuarantineStatus"], Optional[str]]):
        self._fn: Callable[["QuarantineStatus"], Optional[str]] = fn

    def apply(self, state: "QuarantineStatus"):
        return self._fn(state)


class BasicAction(Action):
    """Class for an action that can be done by the user.

    """

    def __init__(self, delta_energy: int, delta_fulfillment: int, message: str):
        def _basic_apply(state: "QuarantineStatus") -> str:
            state.energy += delta_energy
            state.fulfillment += delta_fulfillment
            return message

        super().__init__(_basic_apply)
        self.delta_energy = delta_energy
        self.delta_fulfillment = delta_fulfillment


ACTIONS: Dict[str, Action] = {
    "drink_beer": BasicAction(
        -10, +10, "You feel refreshed, and a little bit light-headed."
    ),  # TODO: drunk_function?
    # "move_room": BasicAction(
    #     -5, 0, "You're here. Now what?"
    # ),  # TODO: decrease fulfillment multiplicatively
    "eat_delivery": BasicAction(
        +5,
        +5,
        "The delivery charge brought the price up a surprising amount. Still... you deserved it.",
    ),  # TODO: decrease energy and fulfillment multiplicatively
    "eat_homecooked": BasicAction(
        +5, +10, "You wonder why you ever order delivery until you look at the clock."
    ),  # TODO: decrease energy from eating too much, increase fulfillment multiplicatively
    "scroll_reddit": BasicAction(
        -5, -5, "....."
    ),  # TODO: decrease energy, decrease fulfillment multiplicatively
    "check_email": BasicAction(
        0, 0, "Nothing."
    ),  # TODO: decrease fulfillment multiplicatively
    "buy_online": BasicAction(
        +10, +20, "TODO"
    ),  # TODO: big decrease in energy and fulfillment
    "binge_netflix": BasicAction(-10, +20, "TODO"),  # TODO: big decrease in fulfillment
    # "cook_food": BasicAction(-20, +20, "TODO"),  # TODO: big increase in fulfillment
    "workout": BasicAction(-20, +5, "TODO"),  # TODO: Fibonacci increase in fulfillment
    # "nap": BasicAction(
    #     +12, -10, "What a waste of time. Refreshing, though."
    # ),  # TODO: drop fulfillment to zero if a portion of day is spent napping
    "zoom_call": BasicAction(-10, 0, "....."),
    # TODO: decrease fulfillment multiplicatively
    "people_watch": BasicAction(0, +15, "TODO"),
    "drink_caffeine": BasicAction(+20, 0, "TODO"),
    # TODO: drink too much, can't sleep/nap for 3 actions
    "listen_to_radio": BasicAction(0, +15, "TODO"),
}


# TIME OF DAY
# Dictionary of day-portion tuples
TIME_OF_DAY = {
    "morning": ("dawn", "mid-morning", "late morning"),
    "afternoon": ("noon", "mid-afternoon", "late afternoon"),
    "night": ("early evening", "dusk", "late evening", "midnight"),
}


def time_of_day_generator():
    for day in range(1, 15):
        for day_portion in TIME_OF_DAY:
            for time in TIME_OF_DAY[day_portion]:
                yield day, time


class QuarantineStatus(object):
    """
    Object for tracking user state. Possible rooms are "bedroom",
    "living room", and "kitchen".
    """

    def __init__(
        self,
        energy: int,
        fulfillment: int,
        action_history: List[Tuple["QuarantineStatus", Action]],
    ):
        self.energy: int = energy
        self.fulfillment: int = fulfillment
        self.current_room = "bedroom"
        self.time_gen = time_of_day_generator()
        self.current_time = next(self.time_gen)
        self._action_history: List[Tuple[QuarantineStatus, Action]] = action_history

    @property
    def available_actions(self) -> List[str]:
        """
        Returns a list of available actions by copying the state and testing if they return None.
        TODO: Separate "invalid" from "will just say something dumb and not do anything"
        """

        # TODO: Performance

        avail = []

        for k, a in ACTIONS.items():
            state_copy = copy.deepcopy(self)
            if a.apply(state_copy) is not None:
                avail.append(k)

        return avail

    # When applying an action, get the Action object from the global ACTIONS
    # dict: `state.apply_action(ACTIONS["drink_beer"])`
    def apply_action(self, action_name: str) -> str:
        old_state = copy.deepcopy(self)

        action: Action = ACTIONS[action_name]
        result = action.apply(self)

        if result is not None:
            self.current_time = next(self.time_gen)
            self._action_history.append((old_state, action))
            return result

        return "Sorry... that's not something you can do now."
