from talon import Context

from . import bindings

context = Context()
context.matches = """
app: /claude/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
and not mode: user.long
and not mode: user.mouse
"""

# south sends only on a long press (fired by the 800ms autorelease), so a
# newline can't be mistaken for a send
bindings.install(context, {
	"dpad_left":      bindings.repeat_key("left"),
	"dpad_right":     bindings.repeat_key("right"),
	"dpad_up":        bindings.repeat_key("up"),
	"dpad_down":      bindings.repeat_key("down"),
	"south":          bindings.by_hold("shift-enter", "shift-enter", "enter"),
	"west":           bindings.by_hold("backspace", "alt-backspace", "cmd-backspace"),
	"east":           bindings.by_hold("escape", "cmd-."),
	"north":          bindings.by_hold("space", "cmd-shift-;"),
	"start":          bindings.by_hold("cmd-shift-o", "cmd-k", "cmd-n"),
	"select":         bindings.by_hold("cmd-w", "cmd-q"),
	"left_shoulder":  bindings.press_key("cmd-shift-`"),
	"right_shoulder": bindings.press_key("cmd-`"),
})
