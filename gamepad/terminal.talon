app: /terminal/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.meeting
-

gamepad(dpad_left:down):
	key(escape)
	key(b:down)
gamepad(dpad_left:up):
	key(b:up)

gamepad(dpad_right:down):
	key(escape)
	key(w:down)
gamepad(dpad_right:up):
	key(w:up)

gamepad(dpad_down:down):
	key(escape)
	key(j:down)
gamepad(dpad_down:up):
	key(j:up)

gamepad(dpad_up:down):
	key(escape)
	key(k:down)
gamepad(dpad_up:up):
	key(k:up)

gamepad(north): key(space)
gamepad(south): key(enter)
gamepad(west): key(backspace)
gamepad(east): key(ctrl-c)

gamepad(l1):
	key(escape)
	key(f12)

gamepad(r1):
	key(tab)

gamepad(select):
	insert("..")
	key(enter)

gamepad(r2):
	key(escape)
   key(shift-A)

gamepad(start):
	insert("cd ")

gamepad(l3:down):
	key(shift:down)
gamepad(l3:up):
	key(shift:up)

gamepad(r3:down):
	key(ctrl:down)
gamepad(r3:up):
	key(ctrl:up)

