from talon import Context, Module, actions, app, scope, ui

mod = Module()
mod.mode("quiet", desc="only the focused quiet app's own commands")

ctx = Context()
ctx.tags = ["user.no_wake_commands"]

quiet_apps = ("lightroom classic", "pianoteq", "organteq", "uvi workstation")

speech_enabled_by_push_to_talk = False


def is_quiet(application) -> bool:
	return any(name in application.name.lower() for name in quiet_apps)


def enter_quiet_mode():
	global speech_enabled_by_push_to_talk
	speech_enabled_by_push_to_talk = False
	for mode in ("sleep", "command", "dictation"):
		actions.mode.disable(mode)
	actions.mode.enable("user.quiet")


def leave_quiet_mode():
	actions.mode.disable("user.quiet")
	actions.mode.enable("command")
	actions.speech.disable()


def on_app_activate(application):
	if is_quiet(application):
		enter_quiet_mode()
	elif "user.quiet" in scope.get("mode"):
		leave_quiet_mode()


def on_ready():
	if actions.speech.enabled():
		actions.speech.disable()
	on_app_activate(ui.active_app())
	ui.register("app_activate", on_app_activate)


app.register("ready", on_ready)


@mod.action_class
class Actions:
	def push_to_talk_start():
		"""enable speech while the push-to-talk key is held"""
		global speech_enabled_by_push_to_talk
		if not actions.speech.enabled():
			actions.speech.enable()
			speech_enabled_by_push_to_talk = True

	def push_to_talk_stop():
		"""disable speech on release, unless it was already on before the press"""
		global speech_enabled_by_push_to_talk
		if speech_enabled_by_push_to_talk:
			actions.speech.disable()
			speech_enabled_by_push_to_talk = False
