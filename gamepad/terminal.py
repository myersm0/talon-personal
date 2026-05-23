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


def select_release(held):
	actions.key("escape")
	actions.key("0")
	actions.key("v")
	actions.key("$")
	actions.key("ctrl-c:2")
	actions.sleep("100ms")
	actions.key("j")


bindings.install(context, {
	"dpad_left":      bindings.repeat_key("left"),
	"dpad_right":     bindings.repeat_key("right"),
	"dpad_up":        bindings.repeat_key("up"),
	"dpad_down":      bindings.repeat_key("down"),
	"north":          bindings.by_hold("space", lambda: actions.insert("y$"), lambda: actions.insert("yy")),
	"south":          bindings.by_hold("enter", "enter", south_long_release),
	"west":           bindings.by_hold("backspace", lambda: actions.insert("d$"), lambda: actions.insert("dd")),
	"east":           bindings.by_hold("ctrl-c", lambda: actions.insert("c$"), lambda: actions.insert("cc")),
	"select":         (bindings.skip_press, select_release),
	"start":          bindings.tap_keys("escape", "f12"),
	"left_shoulder":  bindings.tap_key("cmd-left"),
	"right_shoulder": bindings.tap_key("cmd-right"),
	"left_trigger":   bindings.tap_keys("escape", "g", "g"),
	"right_trigger":  bindings.tap_keys("escape", "G"),
})
