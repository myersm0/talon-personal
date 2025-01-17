from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

ctx_recording1 = Context()
ctx_recording1.matches = """
mode: user.recording
and not mode: user.meeting
"""

@ctx_recording1.action_class("user")
class Recording1Actions:
    def gamepad_press_east():
        actions.key("ctrl-c")
    def gamepad_release_east(held):
        actions.user.unmute()
        actions.mode.disable("user.recording")
        actions.speech.enable()
        print("Waking up.")


ctx_recording2 = Context()
ctx_recording2.matches = """
mode: user.recording
and mode: user.meeting
"""

@ctx_recording2.action_class("user")
class Recording2Actions:
    def gamepad_press_east():
        actions.key("ctrl-c")
    def gamepad_release_east(held):
        actions.user.unmute()
        actions.mode.disable("user.recording")
        print("Not waking up because we're in a meeting.")

