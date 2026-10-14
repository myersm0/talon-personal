from talon import Context, actions

from . import bindings

context = Context()
context.matches = """
app: /terminal/i
app: /term/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
and not mode: user.long
and not mode: user.mouse
"""


def south_long_release():
	actions.key("escape")
	actions.insert("p")


bindings.install(context, {
	"dpad_left":      bindings.repeat_key("left"),
	"dpad_right":     bindings.repeat_key("right"),
	"dpad_up":        bindings.repeat_key("up"),
	"dpad_down":      bindings.repeat_key("down"),
	"north":          bindings.by_hold("space", lambda: actions.insert("y$"), lambda: actions.insert("yy")),
	"south":          bindings.by_hold("enter", "enter", south_long_release),
	"west":           bindings.by_hold("backspace", lambda: actions.insert("d$"), lambda: actions.insert("dd")),
	"east":           bindings.by_hold("ctrl-c", lambda: actions.insert("c$"), lambda: actions.insert("cc")),
	"select":         bindings.tap_keys("escape", "0", "V", "g", "s"),
	"start":          bindings.tap_keys("escape", "g", "b"),
	"left_shoulder":  bindings.tap_keys("ctrl-t", "left", "enter"),
	"right_shoulder": bindings.tap_keys("ctrl-t", "right", "enter"),
})
