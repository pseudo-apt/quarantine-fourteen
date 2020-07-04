from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

import internals

from scenes import intro


def demo(screen):
    screen.set_title("Quarantine Fourteen")

    scenes = []

    # First scene- title sequence
    effects = [
        Cycle(screen, FigletText("WELCOME TO", font="big"), screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("QUARANTINE FOURTEEN", font="big"),
            screen.height // 2 + 3,
        ),
        Stars(screen, (screen.width + screen.height) // 2),
    ]
    screen.play([Scene(effects, 500)])


Screen.wrapper(intro.demo)

Screen.wrapper(demo)
status = internals.QuarantineStatus(100, 100, [])
