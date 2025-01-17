from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_julia = Context()
ctx_julia.matches = """
app: /julia/i
"""

@ctx_julia.action_class("user")
class JuliaActions:
    def gamepad_press_dpad_left():
        actions.user.key_hold("left", "32ms")
    def gamepad_release_dpad_left(held):
        actions.user.key_release("left")

    def gamepad_press_dpad_right():
        actions.user.key_hold("right", "32ms")
    def gamepad_release_dpad_right(held):
        actions.user.key_release("right")

    def gamepad_press_dpad_up():
        actions.skip()
    def gamepad_release_dpad_up(held):
        actions.key("up")

    def gamepad_press_dpad_down():
        actions.skip()
    def gamepad_release_dpad_down(held):
        actions.key("down")

    def gamepad_press_north():
        actions.skip()
    def gamepad_release_north(held):
        actions.key("space")

    def gamepad_press_south():
        actions.skip()
    def gamepad_release_south(held):
        actions.key("enter")

    def gamepad_press_west():
        actions.skip()
    def gamepad_release_west(held):
        actions.key("backspace")

    def gamepad_press_east():
        actions.skip()
    def gamepad_release_east(held):
        actions.key("q")

    def gamepad_press_left_shoulder():
        actions.key("ctrl-pageup")
    def gamepad_release_left_shoulder(held):
        actions.skip()

    def gamepad_press_right_shoulder():
        actions.key("ctrl-pagedown")
    def gamepad_release_right_shoulder(held):
        actions.skip()

    def gamepad_trigger_left(value: float):
        """Gamepad trigger left movement"""
        if value > 0.8:
            actions.key(",")

    def gamepad_trigger_right(value: float):
        """Gamepad trigger right movement"""
        if value > 0.8:
            actions.key(".")

    def gamepad_press_left_stick():
        actions.skip()
    def gamepad_release_left_stick(held):
        actions.key("0")

    def gamepad_press_right_stick():
        actions.skip()
    def gamepad_release_right_stick(held):
        actions.key('$')

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        actions.key("e")

    def gamepad_press_start():
        actions.skip()
    def gamepad_release_start(held):
        actions.key("a")


