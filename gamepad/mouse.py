from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_general = Context()
ctx_general.matches = """
mode: user.mouse
"""

@ctx_general.action_class("user")
class GeneralActions:
	def gamepad_press_south():
		actions.skip()
	def gamepad_release_south(held):
		actions.mouse_click(0)

	def gamepad_press_east():
		actions.skip()
	def gamepad_release_east(held):
		actions.mouse_click(1)

	def gamepad_press_north():
		actions.key("cmd:down")
	def gamepad_release_north(held):
		actions.mouse_click(0)
		actions.key("cmd:up")

	def gamepad_press_west():
		actions.key("shift:down")
	def gamepad_release_west(held):
		actions.mouse_click(0)
		actions.key("shift:up")
