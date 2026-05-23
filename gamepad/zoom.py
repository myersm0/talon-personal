from talon import Context, actions

from . import bindings

context = Context()
context.matches = """
app: /zoom/i
not mode: user.long
and not mode: user.mouse
and not mode: user.recording
"""


def right_stick_release(held):
	if held >= 1:
		actions.key("cmd-shift-a")


def select_release(held):
	if held >= 1:
		actions.key("cmd-q")


bindings.install(context, {
	"right_stick": (bindings.skip_press, right_stick_release),
	"select":      (bindings.skip_press, select_release),
	"start":       bindings.tap_call(actions.user.take_screenshot),
})
