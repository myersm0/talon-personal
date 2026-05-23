from talon import Context

from . import bindings

context = Context()
context.matches = """
app: /terminal/
app: /term/
mode: user.seek
and not mode: user.recording
"""

bindings.install(context, {
	"dpad_left":  bindings.repeat_key("left"),
	"dpad_right": bindings.repeat_key("right"),
	"dpad_up":    bindings.repeat_key("up"),
	"dpad_down":  bindings.repeat_key("down"),
	"north":      bindings.press_key("space"),
	"south":      bindings.press_key("enter"),
	"west":       bindings.press_key("q"),
	"east":       bindings.press_key("$"),
})
