from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_safari = Context()
ctx_safari.matches = """
app: /safari/i
"""

@ctx_safari.action_class("user")
class SafariActions:
	def gamepad_press_dpad_left():
		actions.skip()
	def gamepad_release_dpad_left(held):
		actions.key("left")

	def gamepad_press_dpad_right():
		actions.skip()
	def gamepad_release_dpad_right(held):
		actions.key("right")

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
		actions.key("enter")

	def gamepad_press_south():
		actions.skip()
	def gamepad_release_south(held):
		actions.mouse_click(0)

	def gamepad_press_west():
		actions.skip()
	def gamepad_release_west(held):
		actions.key("escape")

	def gamepad_press_east():
		actions.skip()
	def gamepad_release_east(held):
		actions.key("escape")

