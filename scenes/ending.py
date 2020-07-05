from asciimatics.effects import Print, Cycle, Stars, BannerText, Mirage, Scroll
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def scene(screen):
    scenes = []

    # debrief
    effects = [
        Mirage(
            screen,
            SpeechBubble("You wake up in your bed, in your apartment"),
            screen.height // 2 - 1,
            colour=Screen.COLOUR_WHITE,
        ),
    ]
    scenes.append(Scene(effects, -1))

    effects = [
        Mirage(
            screen,
            SpeechBubble("The world feels different somehow"),
            screen.height // 2 + 1,
            colour=Screen.COLOUR_WHITE,
        ),
    ]
    scenes.append(Scene(effects, -1))

    effects = [
        Mirage(
            screen,
            SpeechBubble(
                "Your phone rings. It's a doctor from your local public health authority."
            ),
            screen.height // 2 + 2,
            colour=Screen.COLOUR_WHITE,
        ),
    ]
    scenes.append(Scene(effects, -1))

    effects = [
        Mirage(
            screen,
            SpeechBubble(
                """"Thanks for adhering to quarantine! Since you didn't develop
any symptoms over the past 14 days, you're free to leave your 
home. Remember to stay 2 meters away from others and to wear a
mask when you're unable to do so!"
""",
                tail="L",
            ),
            screen.height // 2 + 3,
            colour=Screen.COLOUR_WHITE,
        ),
    ]
    scenes.append(Scene(effects, -1))

    effects = [
        Cycle(
            screen, FigletText("THANKS FOR PLAYING", font="big"), screen.height // 2 - 8
        ),
        Cycle(
            screen,
            FigletText("QUARANTINE FOURTEEN", font="big"),
            screen.height // 2 + 3,
        ),
        Stars(screen, (screen.width + screen.height) // 2),
        Print(
            screen,
            SpeechBubble("Press SPACE to continue..."),
            screen.height - 3,
            transparent=False,
            start_frame=30,
        ),
    ]
    scenes.append(Scene(effects, -1))

    effects = [
        Cycle(screen, FigletText("CREDITS", font="big"), screen.height // 2 - 8),
        Stars(screen, (screen.width + screen.height) // 2),
        Print(
            screen,
            SpeechBubble("Press SPACE to continue..."),
            screen.height - 3,
            transparent=False,
            start_frame=30,
        ),
    ]
    scenes.append(Scene(effects, -1))

    effects = [
        Mirage(
            screen,
            SpeechBubble(
                """_  Johanan Idicula  
|                   
|                   
|                   
                    
2 meters            
                    
|                   
|                   
|                   
‾                   
_   David Lougheed  
|                   
|                   
|                   
                    
2 meters            
                    
|                   
|                   
|                   
‾    Marie Payne    """
            ),
            5,
            colour=Screen.COLOUR_WHITE,
        ),
    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes, repeat=False)
