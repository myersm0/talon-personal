from talon import Context, actions

from . import bindings

context = Context()
context.matches = """
app: /safari/i
not mode: user.long
and not mode: user.mouse
and not mode: user.recording
"""

bindings.install(context, {
	"dpad_left":  bindings.tap_key("left"),
	"dpad_right": bindings.tap_key("right"),
	"dpad_up":    bindings.tap_key("up"),
	"dpad_down":  bindings.tap_key("down"),
	"north":      bindings.tap_key("enter"),
	"south":      bindings.tap_call(lambda: actions.mouse_click(0)),
	"west":       bindings.tap_key("escape"),
	"east":       bindings.tap_key("escape"),
})
