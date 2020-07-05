from asciimatics.widgets import Frame, TextBox, Layout, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

# Initial data for the form
form_data = {
    "user_input": "",
}

USER_INPUTS = []

class DemoFrame(Frame):
    def __init__(self, screen, game_text):
        super(DemoFrame, self).__init__(
            screen,
            int(screen.height * 2 // 3),
            int(screen.width * 2 // 3 ),
            data=form_data,
            has_shadow=True,
            has_border=False,
            name="Player input",
        )
        layout = Layout([100])
        self.add_layout(layout)
        self.set_theme("monochrome")
        num_rows = game_text.count("\n")+1
        layout.add_widget(Label(game_text, num_rows))
        layout.add_widget(
            TextBox(
                height=1,
                label="> ",
                name="user_input",
                on_change=self._on_change,
                as_string=True,
            )
        )
        self.fix()

    def _on_change(self):
        self.save()
        if "user_input" in self.data.keys():
            if self.data["user_input"] != "":
                if self.data["user_input"] == "q\n":
                    USER_INPUTS.append(self.data["user_input"])
                    self.reset()
                    self.data = {}
                    raise StopApplication("User quit")
                if self.data["user_input"][-1] == "\n":
                    USER_INPUTS.append(self.data["user_input"])
                    self.reset()
                    self.data = {}
                    raise StopApplication("Next scene")

