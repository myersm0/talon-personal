from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_meeting = Context()
ctx_meeting.matches = """
mode: user.meeting
"""

@ctx_meeting.action_class("user")
class MeetingActions:
    def gamepad_press_left_stick():
        actions.speech.enable()
    def gamepad_release_left_stick(held):
        actions.speech.disable()
