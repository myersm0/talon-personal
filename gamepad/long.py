from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_meeting = Context()
ctx_meeting.matches = """
mode: user.long
and not mode: user.meeting
"""

@ctx_meeting.action_class("user")
class MeetingActions:
	def gamepad_press_select():
		actions.skip()
	def gamepad_release_select(held):
		actions.mimic("set dummy Mike")
	def gamepad_press_start():
		actions.skip()
	def gamepad_release_start(held):
		actions.mimic("set default Mike")
	def gamepad_press_dpad_up():
		actions.skip()
	def gamepad_release_dpad_up(held):
		actions.mimic("window next")
	def gamepad_press_dpad_down():
		actions.skip()
	def gamepad_release_dpad_down(held):
		actions.mimic("window last")
	def gamepad_press_dpad_left():
		actions.skip()
	def gamepad_release_dpad_left(held):
		actions.mimic("focus last")
	def gamepad_press_dpad_right():
		actions.skip()
	def gamepad_release_dpad_right(held):
		actions.mimic("focus last")
	def gamepad_press_north():
		actions.skip()
	def gamepad_release_north(held):
		actions.mimic("window next")
	def gamepad_press_south():
		actions.skip()
	def gamepad_release_south(held):
		actions.mimic("window last")
	def gamepad_press_west():
		actions.skip()
	def gamepad_release_west(held):
		actions.mimic("focus last")
	def gamepad_press_east():
		actions.skip()
	def gamepad_release_east(held):
		actions.mimic("focus last")
	def gamepad_press_left_trigger():
		actions.skip()
	def gamepad_release_left_trigger(held):
		actions.mimic("undo")
	def gamepad_press_right_trigger():
		actions.skip()
	def gamepad_release_right_trigger(held):
		actions.mimic("redo")
