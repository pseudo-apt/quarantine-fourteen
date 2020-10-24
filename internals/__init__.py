import copy
from typing import Callable, Dict, List, Optional, Tuple

from . import asciiart


class Action:
    """
    Generic action class for updating the game state.
    """

    def __init__(self, fn: Callable[["QuarantineStatus"], Optional[str]]):
        self._fn: Callable[["QuarantineStatus"], Optional[str]] = fn

    def apply(self, state: "QuarantineStatus"):
        return self._fn(state)


class BasicAction(Action):
    """Class for an action that can be done by the user."""

    def __init__(self, delta_energy: int, delta_fulfillment: int, message: str):
        def _basic_apply(state: "QuarantineStatus") -> str:
            state.energy += delta_energy
            state.fulfillment += delta_fulfillment
            return message

        super().__init__(_basic_apply)
        self.delta_energy = delta_energy
        self.delta_fulfillment = delta_fulfillment


# Action names
ACTION_GET_SLOSHED = "drink_beer"
ACTION_ORDER_TAKEOUT = "eat_delivery"
ACTION_COOK_FOOD = "eat_homecooked"
ACTION_INFINITE_REDDIT = "scroll_reddit"
ACTION_REFRESH_INBOX = "check_email"
ACTION_ONLINE_SHOPPING = "buy_online"
ACTION_NETFLIX_AND_CHILL_W_YOURSELF = "binge_netflix"
ACTION_BRO_SPLIT_IT_UP = "workout"
ACTION_VIDEO_CHAT_WITH_THE_FAM = "zoom_call"
ACTION_STARE_OUT_WINDOW = "people_watch"
ACTION_COFFEEDENCE = "drink_caffeine"
ACTION_DANCE_LIKE_NO_ONES_WATCHING = "listen_to_radio"

# ASCII art associated with each action
ACTIONS_ASCII_ART: Dict[str, str] = {
    ACTION_GET_SLOSHED: asciiart.ACTION_GET_SLOSHED_SCENE,
    ACTION_ORDER_TAKEOUT: asciiart.ACTION_ORDER_TAKEOUT_SCENE,
    ACTION_COOK_FOOD: asciiart.ACTION_COOK_FOOD_SCENE,
    ACTION_INFINITE_REDDIT: asciiart.ACTION_INFINITE_REDDIT_SCENE,
    ACTION_REFRESH_INBOX: asciiart.ACTION_REFRESH_INBOX_SCENE,
    ACTION_ONLINE_SHOPPING: asciiart.ACTION_ONLINE_SHOPPING_SCENE,
    ACTION_NETFLIX_AND_CHILL_W_YOURSELF: asciiart.ACTION_NETFLIX_AND_CHILL_W_YOURSELF_SCENE,
    ACTION_BRO_SPLIT_IT_UP: asciiart.ACTION_BRO_SPLIT_IT_UP_SCENE,
    ACTION_VIDEO_CHAT_WITH_THE_FAM: asciiart.ACTION_VIDEO_CHAT_WITH_THE_FAM_SCENE,
    ACTION_STARE_OUT_WINDOW: asciiart.ACTION_STARE_OUT_WINDOW_SCENE,
    ACTION_COFFEEDENCE: asciiart.ACTION_COFFEEDENCE_SCENE,
    ACTION_DANCE_LIKE_NO_ONES_WATCHING: asciiart.ACTION_DANCE_LIKE_NO_ONES_WATCHING_SCENE,
}

# Action properties
ACTIONS: Dict[str, Action] = {
    ACTION_GET_SLOSHED: BasicAction(
        -10, +10, "You feel refreshed, and a little bit light-headed."
    ),  # TODO: drunk_function?
    # "move_room": BasicAction(
    #     -5, 0, "You're here. Now what?"
    # ),  # TODO: decrease fulfillment multiplicatively
    ACTION_ORDER_TAKEOUT: BasicAction(
        +5,
        +5,
        "The delivery charge brought the price up a surprising amount. Still... you deserved it.",
    ),  # TODO: decrease energy and fulfillment multiplicatively
    ACTION_COOK_FOOD: BasicAction(
        +5, +10, "You wonder why you ever order delivery until you look at the clock."
    ),  # TODO: decrease energy from eating too much, increase fulfillment multiplicatively
    ACTION_INFINITE_REDDIT: BasicAction(
        -5,
        -5,
        "You're getting really good at recognizing reposts. Those cat gifs are cute, though.",
    ),  # TODO: decrease energy, decrease fulfillment multiplicatively
    ACTION_REFRESH_INBOX: BasicAction(
        0,
        0,
        'Another corporate email about "troubling and uncertain times" and a 20% off clearance sale.',
    ),  # TODO: decrease fulfillment multiplicatively
    ACTION_ONLINE_SHOPPING: BasicAction(
        +10,
        +20,
        "How are you spending the same amount and you can't even leave your apartment?",
    ),  # TODO: big decrease in energy and fulfillment
    ACTION_NETFLIX_AND_CHILL_W_YOURSELF: BasicAction(
        -10,
        +20,
        "Another episode down of a show you'll watch most of and then forget.\n "
        "Not the worst use of time.",
    ),  # TODO: big decrease in fulfillment
    # "cook_food": BasicAction(-20, +20, "TODO"),  # TODO: big increase in fulfillment
    ACTION_BRO_SPLIT_IT_UP: BasicAction(
        -20, +5, "You're tired, but in a good way."
    ),  # TODO: Fibonacci increase in fulfillment
    # "nap": BasicAction(
    #     +12, -10, "What a waste of time. Refreshing, though."
    # ),  # TODO: drop fulfillment to zero if a portion of day is spent napping
    ACTION_VIDEO_CHAT_WITH_THE_FAM: BasicAction(
        -10, 0, "Sorry, could you repeat that? The call froze."
    ),
    # TODO: decrease fulfillment multiplicatively
    ACTION_STARE_OUT_WINDOW: BasicAction(
        0, +15, "A few people drift by, maybe 30% slower than they'd usually walk."
    ),
    ACTION_COFFEEDENCE: BasicAction(
        +20,
        0,
        "The buzzing at the base of your skull is louder. \n"
        "Maybe you should get it looked at?",
    ),
    # TODO: drink too much, can't sleep/nap for 3 actions
    ACTION_DANCE_LIKE_NO_ONES_WATCHING: BasicAction(
        0,
        +15,
        "For better or for worse, you're now more informed about the \n"
        "state of the world. Some numbers are up; others are down.",
    ),
}


# TIME OF DAY
# Dictionary of day-portion tuples
TIME_OF_DAY = {
    "morning": ("dawn", "mid-morning", "late morning"),
    "afternoon": ("noon", "mid-afternoon", "late afternoon"),
    "night": ("early evening", "dusk", "late evening", "midnight"),
}


def time_of_day_generator():
    for day in range(0, 15):
        for day_portion in TIME_OF_DAY:
            for time in TIME_OF_DAY[day_portion]:
                yield day + 1, time


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
        self.day_count, self.current_time = next(self.time_gen)
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

        action: Action = ACTIONS[action_name]
        result = action.apply(self)

        if result is not None:
            # TODO: handle exception when no more iteration can be done
            self.day_count, self.current_time = next(self.time_gen)
            return result

        return "Sorry... that's not something you can do now."
