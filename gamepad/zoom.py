from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_zoom = Context()
ctx_zoom.matches = """
app: /zoom/i
"""

@ctx_zoom.action_class("user")
class ZoomActions:
    def gamepad_press_right_stick():
        actions.skip()
    def gamepad_release_right_stick(held):
        if held >= 1:
            actions.key("cmd-shift-a")

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        if held >= 1:
            actions.key("cmd-q")

    def gamepad_press_start():
        actions.skip()
    def gamepad_release_start(held):
        actions.user.take_screenshot()

