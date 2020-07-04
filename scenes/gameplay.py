from asciimatics.widgets import Frame, TextBox, Layout, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

# Initial data for the form
form_data = {
    "user_input": "",
}


class DemoFrame(Frame):
    def __init__(self, screen, game_text):
        super(DemoFrame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        data=form_data,
                                        has_shadow=True,
                                        has_border=False,
                                        name="Player input")
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        self.set_theme("monochrome")
        layout.add_widget(Label(game_text), 1)
        layout.add_widget(
            TextBox(height=1,
                 label="> ",
                 name="user_input",
                 on_change=self._on_change,
                 as_string=True), 1)
        self.fix()

    def _on_change(self):
        self.save()
        if "user_input" in self.data.keys():
            if self.data["user_input"] == "quit\n":
                raise StopApplication("User quit")
            if "\n" in self.data["user_input"]:
                self.reset()
                raise NextScene()

