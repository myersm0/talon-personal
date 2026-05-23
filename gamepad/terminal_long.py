from talon import Context

from . import bindings

context = Context()
context.matches = """
app: /terminal/i
app: /term/i
mode: user.long
and not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
and not mode: user.mouse
"""

bindings.install(context, {
	"dpad_left":      bindings.tap_keys("ctrl-a", "h"),
	"dpad_right":     bindings.tap_keys("ctrl-a", "l"),
	"dpad_up":        bindings.tap_keys("ctrl-a", "k"),
	"dpad_down":      bindings.tap_keys("ctrl-a", "j"),
	"left_shoulder":  bindings.tap_keys("escape", "u"),
	"right_shoulder": bindings.tap_keys("escape", "ctrl-r"),
})
