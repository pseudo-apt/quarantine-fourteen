from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError
import sys

import internals


from scenes import intro, gameplay, ending


def demo(screen):
    screen.set_title("Quarantine Fourteen")
    intro.demo(screen)

    scenes = []

    while True:
        game_text = "It's 8AM. You get up out of bed. What do you do?"
        new_screen = gameplay.DemoFrame(screen, game_text)
        effects = [
            new_screen,
        ]
        scenes.append(Scene(effects, -1))

        screen.play(scenes, repeat=False)

        user_input = new_screen.data["user_input"]

        if user_input == "quit\n":
            sys.exit(0)

    ending.scene(screen)


Screen.wrapper(demo)

status = internals.QuarantineStatus(100, 100, [])
