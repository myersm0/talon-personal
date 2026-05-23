from talon import Context

from . import bindings

context = Context()
context.matches = """
not app: /terminal/i
and not app: /term/i
and not app: /kbr/i
and not app: /zoom/i
and not app: /safari/i
and not app: /steam/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
and not mode: user.long
and not mode: user.mouse
"""

bindings.install(context, {
	"dpad_left":      bindings.repeat_key("left"),
	"dpad_right":     bindings.repeat_key("right"),
	"dpad_up":        bindings.repeat_key("up"),
	"dpad_down":      bindings.repeat_key("down"),
	"north":          bindings.repeat_key("space"),
	"south":          bindings.repeat_key("enter"),
	"west":           bindings.repeat_key("backspace"),
	"east":           bindings.repeat_key("."),
	"select":         bindings.by_hold("cmd-w", "cmd-q"),
	"start":          bindings.by_hold("cmd-t", "cmd-n", "cmd-shift-n"),
	"left_shoulder":  bindings.press_key("ctrl-shift-tab"),
	"right_shoulder": bindings.press_key("ctrl-tab"),
})
