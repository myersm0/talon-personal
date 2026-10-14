from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_zoom = Context()
ctx_zoom.matches = """
app: /pianoteq/i
app: /organteq/i
mode: command
mode: user.quiet
"""

@ctx_zoom.action_class("user")
class ModarttActions:
	def gamepad_press_left_shoulder():
		actions.skip()
	def gamepad_release_left_shoulder(held):
		actions.key("p")
	def gamepad_press_right_shoulder():
		actions.skip()
	def gamepad_release_right_shoulder(held):
		actions.key("n")

