app: /terminal/i
mode: user.seek
-

gamepad(dpad_left:down): key(left:down)
gamepad(dpad_left:up): key(left:up)
gamepad(dpad_right:down): key(right:down)
gamepad(dpad_right:up): key(right:up)
gamepad(dpad_down:down): key(down:down)
gamepad(dpad_down:up): key(down:up)
gamepad(dpad_up:down): key(up:down)
gamepad(dpad_up:up): key(up:up)

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

