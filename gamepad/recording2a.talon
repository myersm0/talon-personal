mode: user.recording
and not mode: user.meeting
-

gamepad(east:down):
	key(ctrl-c)

gamepad(east:up):
	mode.disable("user.recording")
	speech.enable()
	print("waking up")




