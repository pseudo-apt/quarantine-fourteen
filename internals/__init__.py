from typing import List

# ACTIONS
# Format: (energy change, fulfillment change, repetitive effect)


class Action(object):
    """Class for an action that can be done by the user.

    """

    def __init__(self, delta_energy, delta_fulfillment):
        super(Action, self).__init__()
        self.delta_energy = delta_energy
        self.delta_fulfillment = delta_fulfillment


ACTIONS = {
    "drink_beer": Action(-10, +10),  # TODO: drunk_function?
    "move_room": Action(-5, 0),  # TODO: decrease fulfillment multiplicatively
    "eat_delivery": Action(
        +5, +5
    ),  # TODO: decrease energy and fulfillment multiplicatively
    "eat_homecooked": Action(
        +5, +10
    ),  # TODO: decrease energy from eating too much, increase fulfillment multiplicatively
    "screen_time": Action(
        -5, -5
    ),  # TODO: decrease energy, decrease fulfillment multiplicatively
    "check_email": Action(0, 0),  # TODO: decrease fulfillment multiplicatively
    "buy_online": Action(+10, +20),  # TODO: big decrease in energy and fulfillment
    "binge_netflix": Action(-10, +20),  # TODO: big decrease in fulfillment
    "cook_food": Action(-20, +20),  # TODO: big increase in fulfillment
    "workout": Action(-20, +5),  # TODO: Fibonacci increase in fulfillment
    "nap": Action(
        +12, -10
    ),  # TODO: drop fulfillment to zero if a portion of day is spent napping
    "zoom_call": Action(-10, 0),
    # TODO: decrease fulfillment multiplicatively
    "people_watch": Action(0, +15),
    "drink_caffeine": Action(+20, 0),
    # TODO: drink too much, can't sleep/nap for 3 actions
    "listen_to_radio": Action(0, +15),
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
    """Object for tracking user state.

    """

    def __init__(self, energy: int, fulfillment: int, action_history: List[Action]):
        self.energy = energy
        self.fulfillment = fulfillment
        self.time_gen = time_of_day_generator()
        self.current_time = next(self.time_gen)
        self.action_history = action_history

    # When applying an action, get the Action object from the global ACTIONS
    # dict: `state.apply_action(ACTIONS["drink_beer"])`
    def apply_action(self, action_name: str) -> bool:
        action: Action = ACTIONS[action_name]
        self.energy += action.delta_energy
        self.fulfillment += action.delta_fulfillment
        self.current_time = next(self.time_gen)
        self.action_history.append(action)
        return True
