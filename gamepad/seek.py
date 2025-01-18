from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_seek = Context()
ctx_seek.matches = """
app: /terminal/
app: /term/
and mode: user.seek
and not mode: user.recording
"""

@ctx_seek.action_class("user")
class SeekActions:
    def gamepad_press_dpad_left():
        actions.user.key_hold("left")
    def gamepad_release_dpad_left(held):
        actions.user.key_release("left")

    def gamepad_press_dpad_right():
        actions.user.key_hold("right")
    def gamepad_release_dpad_right(held):
        actions.user.key_release("right")

    def gamepad_press_dpad_up():
        actions.user.key_hold("up")
    def gamepad_release_dpad_up(held):
        actions.user.key_release("up")

    def gamepad_press_dpad_down():
        actions.user.key_hold("down")
    def gamepad_release_dpad_down(held):
        actions.user.key_release("down")

    def gamepad_press_north():
        actions.key("space")
    def gamepad_release_north(held):
        actions.skip()

    def gamepad_press_south():
        actions.key("enter")
    def gamepad_release_south(held):
        actions.skip()

    def gamepad_press_west():
        actions.key("q")
    def gamepad_release_west(held):
        actions.skip()

    def gamepad_press_east():
        actions.key("$")
    def gamepad_release_east(held):
        actions.skip()

