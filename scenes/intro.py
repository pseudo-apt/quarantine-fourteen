from random import randint
from asciimatics.effects import Print, Cycle, Stars
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, \
    ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

def demo(screen):
	scenes = []

	# First scene: title sequence
	effects = [
		Cycle(
			screen,
			FigletText("WELCOME TO", font='big'),
			screen.height // 2 - 8),
		Cycle(
			screen,
			FigletText("QUARANTINE FOURTEEN", font='big'),
			screen.height // 2 + 3),
		Stars(screen, (screen.width + screen.height) // 2),
		Print(screen,
			SpeechBubble("Press SPACE to continue..."),
			screen.height - 3,
			transparent=False,
			start_frame=70)
	]
	scenes.append(Scene(effects, 500))
	#scenes.append(Scene(effects, -1))

	screen.play(scenes)
