from talon import Context, actions

from . import bindings


def east_press():
	actions.key("ctrl-c")


def make_east_release(wake_speech):
	def release():
		actions.user.unmute()
		actions.mode.disable("user.recording")
		if wake_speech:
			actions.speech.enable()
	return release


context_recording_no_meeting = Context()
context_recording_no_meeting.matches = """
mode: user.recording
and not mode: user.meeting
and not mode: user.long
"""

bindings.install(context_recording_no_meeting, {
	"east": bindings.hold(east_press, make_east_release(wake_speech=True)),
})


context_recording_in_meeting = Context()
context_recording_in_meeting.matches = """
mode: user.recording
and mode: user.meeting
"""

bindings.install(context_recording_in_meeting, {
	"east": bindings.hold(east_press, make_east_release(wake_speech=False)),
})
