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

    quarantine_status = internals.QuarantineStatus(10, 10, [])

    game_text = "It's 8AM. You get up out of bed. What do you do?"
    action_index = 0
    options = ""
    action_names = [a for a in internals.ACTIONS.keys()]
    for action in action_names:
        action_name = action.replace("_", " ")
        options += f"\n{action_index}- {action_name}"
        action_index += 1
    game_text += options

    while True:
        scenes = []
        new_screen = gameplay.DemoFrame(screen, game_text)
        effects = [
            new_screen,
        ]
        scenes.append(Scene(effects, -1))

        screen.play(scenes, repeat=False)

        user_input = gameplay.USER_INPUTS[-1]
        if user_input == "q\n":
            sys.exit(0)

        is_valid = validate_user_input(user_input.rstrip())
        if not is_valid:
            continue
        user_choice = int(user_input)

        quarantine_status.apply_action(action_names[user_choice])

        game_text = f"It's {quarantine_status.current_time[1]}. You're in {quarantine_status.current_room}.\n Your energy is {quarantine_status.energy}% and your filfillment is {quarantine_status.fulfillment}%. What do you do?"
        game_text += options


    ending.scene(screen)


def validate_user_input(user_input):
    valid = False
    if user_input.isnumeric():
        user_choice = int(user_input)
        if user_choice >= 0 and user_choice < len(internals.ACTIONS):
            valid = True
    return valid


if __name__ == "__main__":

    # Render the game
    Screen.wrapper(demo)

    status = internals.QuarantineStatus(100, 100, [])
