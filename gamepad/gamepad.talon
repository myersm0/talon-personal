app: firefox
app: /libreoffice/
app: gedit
app: xed
app: xviewer
app: pavucontrol
not mode: user.seek
and not mode: user.symbol
and not mode: user.meeting
-

gamepad(dpad_left:down): key(left:down)
gamepad(dpad_left:up): key(left:up)
gamepad(dpad_right:down): key(right:down)
gamepad(dpad_right:up): key(right:up)
gamepad(dpad_down:down): key(down:down)
gamepad(dpad_down:up): key(down:up)
gamepad(dpad_up:down): key(up:down)
gamepad(dpad_up:up): key(up:up)

gamepad(north:down): key(space:down)
gamepad(north:up): key(space:up)
gamepad(south:down): key(enter:down)
gamepad(south:up): key(enter:up)
gamepad(west:down): key(backspace:down)
gamepad(west:up): key(backspace:up)
gamepad(east:down): key(.:down)
gamepad(east:up): key(.:up)

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


