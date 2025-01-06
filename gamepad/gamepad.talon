app: firefox
app: brave
app: /workbench/i
app: /libreoffice/i
app: /soffice/i
app: gedit
app: TextEdit
app: xviewer
app: pavucontrol
app: /nemo/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
#and not mode: user.meeting
-

gamepad(dpad_left:down):
	key(escape)
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

gamepad(north:down): user.key_hold("space")
gamepad(north:up): user.key_release("space")
gamepad(south:down): user.key_hold("enter")
gamepad(south:up): user.key_release("enter")
gamepad(west:down): user.key_hold("backspace")
gamepad(west:up): user.key_release("backspace")
gamepad(east:down): user.key_hold(".")
gamepad(east:up): user.key_release(".")

gamepad(l1):	key(ctrl-pageup)
gamepad(r1):	key(ctrl-pagedown)

gamepad(l3:down):
	key(shift:down)
gamepad(l3:up):
	key(shift:up)

gamepad(r3:down):
	key(ctrl:down)
gamepad(r3:up):
	key(ctrl:up)

