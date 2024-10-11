mode: user.recording
and mode: user.meeting
-

gamepad(east:down):
	key(ctrl-c)

gamepad(east:up):
	mode.disable("user.recording")
	print("not waking up because we're in a meeting")


