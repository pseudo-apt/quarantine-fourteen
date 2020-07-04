from asciimatics.screen import Screen

from scenes import intro

import internals

from scenes import intro


def demo(screen):
	screen.set_title("Quarantine Fourteen")
	intro.demo(screen)

Screen.wrapper(demo)
status = internals.QuarantineStatus(100, 100, [])
