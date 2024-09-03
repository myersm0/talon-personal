app: celluloid
not mode: user.seek
and not mode: user.symbol
and not mode: user.meeting
-

gamepad(dpad_left:down): key(left:down)
gamepad(dpad_left:up): key(left:up)
gamepad(dpad_right:down): key(right:down)
gamepad(dpad_right:up): key(right:up)
gamepad(dpad_down:down): key(/:down)
gamepad(dpad_down:up): key(/:up)
gamepad(dpad_up:down): key(*:down)
gamepad(dpad_up:up): key(*:up)

gamepad(north:down): key(space)
gamepad(south:down): key(space)
gamepad(west:down): key(q)
gamepad(east:down): key(m)

gamepad(l1):	key(<)
gamepad(r1):	key(>)

gamepad(l2:down):
	key(shift:down)
	key(left:down)
gamepad(l2:up):
	key(shift:up)
	key(left:up)

gamepad(r2:down):
	key(shift:down)
	key(right:down)
gamepad(r2:up):
	key(shift:up)
	key(right:up)

gamepad(select):
	key(alt--)

gamepad(start):
	key(alt-shift-+)
