not mode: recording
-

take note:
	user.mute()
	speech.disable()
	mode.enable("user.recording")
	user.run_external_command("take_note")

take context:
	user.mute()
	speech.disable()
	mode.enable("user.recording")
	user.run_external_command("take_context")


