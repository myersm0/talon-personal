mode: user.seek
and not mode: user.recording
-

key(enter):
	mode.disable("user.seek")
	key(enter)

key(q):
	mode.disable("user.seek")
	key(q)
