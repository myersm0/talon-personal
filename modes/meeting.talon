mode: user.meeting
-
^(command mode|end of meeting)$:
	user.set_default_mic()
	speech.enable()
	mode.disable("user.meeting")
	mode.enable("command")

key(f5:down):
	speech.enable()

key(f5:up):
	speech.disable()

gamepad(l3:down):
	speech.enable()
gamepad(l3:up):
	speech.disable()


