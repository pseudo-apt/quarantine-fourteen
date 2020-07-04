from asciimatics.effects import Print, Cycle, Stars, BannerText, Mirage, Scroll
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, \
    ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen

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
			start_frame=30)
	]
	scenes.append(Scene(effects, -1))

	# Quick gameplay mechanics explanation
	effects = [
		Print(screen,
			SpeechBubble("To quit the game at any time, press q. To proceed, press SPACE."),
			screen.height - 3,
			transparent=False)
	]
	scenes.append(Scene(effects, -1))

	# Second scene: text
	effects = [
		Mirage(
			screen,
			SpeechBubble("You wake up in your bed, in your apartment"),
			screen.height // 2 - 1,
			colour=Screen.COLOUR_WHITE),
	]
	scenes.append(Scene(effects, -1))

	effects = [
		Mirage(
			screen,
			SpeechBubble("The world feels different somehow"),
			screen.height // 2 + 1,
			colour=Screen.COLOUR_WHITE),
	]
	scenes.append(Scene(effects, -1))

	effects = [
		Mirage(
			screen,
			SpeechBubble("Your phone rings. It's a doctor from your local public health authority."),
			screen.height // 2 + 2,
			colour=Screen.COLOUR_WHITE),
	]
	scenes.append(Scene(effects, -1))

	effects = [
		Mirage(
			screen,
			SpeechBubble("\"Thanks for dropping by yesterday. Your results should be in \nwithin the next few days. Please keep yourself isolated \nfor the next 14 days inside your home.\"", tail="L"),
			screen.height // 2 + 3,
			colour=Screen.COLOUR_WHITE),
	]
	scenes.append(Scene(effects, -1))

	screen.play(scenes, repeat=False)
