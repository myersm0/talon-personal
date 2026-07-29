from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

from . import bindings

context = Context()
context.matches = """
app: /kbr/i
and not mode: user.long
"""

bindings.install(context, {
	"dpad_left":       bindings.repeat_key("left"),
	"dpad_right":       bindings.repeat_key("right"),
	"dpad_up":       bindings.tap_key("up"),
	"dpad_down":       bindings.tap_key("down"),
	"north":       bindings.tap_key("space"),
	"south":       bindings.tap_key("enter"),
	"east":       bindings.tap_key("q"),
	"left_shoulder":       bindings.tap_keys("ctrl-pagedown"),
	"right_shoulder":       bindings.tap_keys("ctrl-pageup"),
})




