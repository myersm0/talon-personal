app: /terminal/i
app: /term/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
#and not mode: user.meeting
-

gamepad(dpad_left:down):
	key(escape)
	key(b:down)
	user.key_hold("b")
gamepad(dpad_left:up):
	user.key_release("b")

gamepad(dpad_right:down):
	key(escape)
	user.key_hold("w")
gamepad(dpad_right:up):
	user.key_release("w")

gamepad(dpad_down:down):
	key(escape)
	user.key_hold("j")
gamepad(dpad_down:up):
	user.key_release("j")

gamepad(dpad_up:down):
	key(escape)
	user.key_hold("k")
gamepad(dpad_up:up):
	user.key_release("k")

gamepad(north:down): key(space:down)
gamepad(north:up): key(space:up)
gamepad(south:down): key(enter:down)
gamepad(south:up): key(enter:up)
gamepad(west:down): user.key_hold("backspace")
gamepad(west:up): user.key_release("backspace")
gamepad(east:down): key(ctrl-c:down)
gamepad(east:up): key(ctrl-c:up)

gamepad(l1):
	key(escape)
	key(f12)

gamepad(l2):
	key(escape)
	key(0)
	key(v)
	key($)
	key(ctrl-c:2)
	sleep(100ms)
	key(j)

gamepad(r1):
	key(tab)

gamepad(select):
	insert("cd ..")
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

