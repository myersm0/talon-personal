mode: user.seek
and not mode: user.recording
-

gamepad(dpad_left:down):
	key(escape)
	key(b:down)
	user.key_hold("left")
gamepad(dpad_left:up):
	user.key_release("left")

gamepad(dpad_right:down):
	key(escape)
	user.key_hold("right")
gamepad(dpad_right:up):
	user.key_release("right")

gamepad(dpad_down:down):
	key(escape)
	user.key_hold("down")
gamepad(dpad_down:up):
	user.key_release("down")

gamepad(dpad_up:down):
	key(escape)
	user.key_hold("up")
gamepad(dpad_up:up):
	user.key_release("up")

gamepad(north:down): key(space)
gamepad(south:down): key(enter)
gamepad(west:down): key(q)
gamepad(east:down): key("$")

key(enter):
	mode.disable("user.seek")
	key(enter)

key(q):
	mode.disable("user.seek")
	key(q)

