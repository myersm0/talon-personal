app: julia
-

gamepad(north:down): key(space)
gamepad(south:down): key(enter)
gamepad(west:down): key(backspace)
gamepad(east:down): key(q)

gamepad(dpad_left:down): user.key_hold("left", "32ms")
gamepad(dpad_left:up): user.key_release("left")
gamepad(dpad_right:down): user.key_hold("right", "32ms")
gamepad(dpad_right:up): user.key_release("right")
gamepad(dpad_down:down): key(down:down)
gamepad(dpad_down:up): key(down:up)
gamepad(dpad_up:down): key(up:down)
gamepad(dpad_up:up): key(up:up)

gamepad(l1):	key(ctrl-pagedown)
gamepad(r1):	key(ctrl-pageup)

gamepad(l2:down):
	key(,:down)
gamepad(l2:up):
	key(,:up)

gamepad(r2:down):
	key(.:down)
gamepad(r2:up):
	key(.:up)

gamepad(l3:down):
	key(0:down)
gamepad(l3:up):
	key(0:up)

gamepad(r3:down):
	key($:down)
gamepad(r3:up):
	key($:up)

gamepad(select): key(e)
gamepad(start): key(a)


