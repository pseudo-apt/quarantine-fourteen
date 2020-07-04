# ACTIONS
# Format: (energy change, fulfillment change, repetitive effect)

DRINK_BEER = (
    -10,
    +10,
    # TODO: drunk_function?
)
MOVE_ROOM = (
    -5,
    0,
    # TODO: decrease fulfillment multiplicatively
)

EAT_DELIVERY = (
    +5,
    +5,
    # TODO: decrease energy and fulfillment multiplicatively
)

EAT_HOMECOOKED = (
    +5,
    +10,
    # TODO: decrease energy from eating too much, increase fulfillment multiplicatively
)

SCREEN_TIME = (
    -5,
    -5,
    # TODO: decrease energy, decrease fulfillment multiplicatively
)

CHECK_EMAIL = (
    0,
    0,
    # TODO: decrease fulfillment multiplicatively
)

BUY_ONLINE = (
    +10,
    +20,
    # TODO: big decrease in energy and fulfillment
)

NETFLIX_BINGING = (
    -10,
    20,
    # TODO: big decrease in fulfillment
)

COOKING = (
    -20,
    +20,
    # TODO: big increase in fulfillment
)

WORKOUT = (
    -20,
    +5,
    # TODO: Fibonacci increase in fulfillment
)

NAP = (
    +12,
    -10,
    # TODO: drop fulfillment to zero if a portion of day is spent napping
)

ZOOM_CALL = (
    -10,
    0,
    # TODO: decrease fulfillment multiplicatively
)

PEOPLE_WATCH = (
    0,
    +15,
)

DRINK_CAFFEINE = (
    +20,
    0,
    # TODO: drink too much, can't sleep/nap for 3 actions
)

LISTEN_TO_RADIO = (
    0,
    +15,
)


# TIME OF DAY
# Dictionary of day-portion tuples
TIME_OF_DAY = {
    "morning": ("dawn", "mid-morning"),
    "afternoon": ("noon", "mid-afternoon"),
    "night": ("6 pm", "8 pm", "10 pm", "midnight"),
}


class QuarantineStatus:
    """Object for tracking user state.

    """

    def __init__(self, energy, fulfillment):
        self.energy = energy
        self.fulfillment = fulfillment
