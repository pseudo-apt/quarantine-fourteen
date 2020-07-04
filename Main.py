from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("WELCOME TO", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("QUARANTINE FOURTEEN", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)

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

# TIME OF DAY
TIME_OF_DAY = {
    "morning": ("dawn", "mid-morning"),
    "afternoon": ("noon", "mid-afternoon"),
    "night": ("6 pm", "8 pm", "10 pm", "midnight"),
}
