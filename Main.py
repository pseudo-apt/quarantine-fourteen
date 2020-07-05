from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError
import sys

import internals


from scenes import intro, gameplay, ending

def demo(screen):
    """
	Renders the intro sequence, and the user input game screens
    """
    screen.set_title("Quarantine Fourteen")
    intro.demo(screen)

    scenes = []

    game_text = "It's 8AM. You get up out of bed. What do you do?"
    action_index = 0
    for action in internals.ACTIONS.keys():
        action_name = action.replace('_', ' ')
        game_text += f"\n{action_index}- {action_name}"
        action_index += 1

    while True:
        new_screen = gameplay.DemoFrame(screen, game_text)
        effects = [
            new_screen,
        ]
        scenes.append(Scene(effects, -1))

        screen.play(scenes, repeat=False)

        user_input = gameplay.USER_INPUTS[-1]
        if user_input == "q\n":
            sys.exit(0)

        is_valid = validate_user_input(user_input)
        if not is_valid:
            continue
        user_choice = int(user_input)

    ending.scene(screen)

def validate_user_input(user_input):
    valid = False
    if user_input.isnumeric():
        user_choice = int(user_input)
        if user_choice >= 0 and user_choice < len(ACTIONS):
            valid = True
    return valid
        

if __name__ == "__main__":

    # Render the game
    Screen.wrapper(demo)

    status = internals.QuarantineStatus(100, 100, [])

