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
	def gamepad_press_right_stick():
		actions.skip()
	def gamepad_release_right_stick(held):
		actions.mimic("set default Mike")
