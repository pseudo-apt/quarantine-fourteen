from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError
import sys

import internals

from scenes import intro, gameplay

def demo(screen):
    """
	Renders the intro sequence, and the user input game screens
    """
    screen.set_title("Quarantine Fourteen")
    intro.demo(screen)

    scenes = []

    rounds = 0
    while True:
        rounds += 1
        game_text = "It's 8AM. You get up out of bed. What do you do?"
        new_screen = gameplay.DemoFrame(screen, game_text)
        effects = [
            new_screen,
        ]
        scenes.append(Scene(effects, -1))

        screen.play(scenes, repeat=False)

        user_input = gameplay.USER_INPUTS[-1]

        if user_input == "quit\n":
            sys.exit(0)


def process_user_input(user_input: str):
    """
        Process what the user input and try to translate it into an action
    """
    input_lowercase = user_input.lower().rstrip()


if __name__ == "__main__":

    # Render the game
    Screen.wrapper(demo)

    status = internals.QuarantineStatus(100, 100, [])

