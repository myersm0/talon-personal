from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_general = Context()
ctx_general.matches = """
not app: /terminal/i
and not app: /term/i
and not app: /julia/i
and not app: /zoom/i
and not app: /safari/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
"""

@ctx_general.action_class("user")
class GeneralActions:
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
        actions.user.key_hold("space")
    def gamepad_release_north(held):
        actions.user.key_release("space")

    def gamepad_press_south():
        actions.user.key_hold("enter")
    def gamepad_release_south(held):
        actions.user.key_release("enter")

    def gamepad_press_west():
        actions.user.key_hold("backspace")
    def gamepad_release_west(held):
        actions.user.key_release("backspace")

    def gamepad_press_east():
        actions.user.key_hold(".")
    def gamepad_release_east(held):
        actions.user.key_release(".")

    def gamepad_press_left_shoulder():
        actions.key("ctrl-pagedown")
    def gamepad_release_left_shoulder(held):
        actions.skip()

    def gamepad_press_right_shoulder():
        actions.key("ctrl-pageup")
    def gamepad_release_right_shoulder(held):
        actions.skip()

    def gamepad_press_left_stick():
        actions.key("shift:down")
    def gamepad_release_left_stick(held):
        actions.key("shift:up")

    def gamepad_press_right_stick():
        actions.key("cmd:down")
    def gamepad_release_right_stick(held):
        actions.key("cmd:up")

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        if held == 0:
            actions.key("cmd-w")
        else:
            actions.key("cmd-q")

    def gamepad_press_start():
        actions.skip()
    def gamepad_release_start(held):
        if held == 0:
            actions.key("cmd-t")
        elif held == 1:
            actions.key("cmd-n")
        elif held == 2:
            actions.key("cmd-shift-n")


