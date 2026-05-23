from talon import Context, actions

from . import bindings

context = Context()
context.matches = """
mode: user.meeting
and not mode: user.long
and not mode: user.mouse
and not mode: user.recording
"""

bindings.install(context, {
	"left_stick": bindings.hold(actions.speech.enable, actions.speech.disable),
})
