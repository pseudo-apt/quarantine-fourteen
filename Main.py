from asciimatics.screen import Screen

from scenes import intro

def demo(screen):
	screen.set_title("Quarantine Fourteen")
	intro.demo(screen)

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
