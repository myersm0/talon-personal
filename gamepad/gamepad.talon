not app: /terminal/i
not app: /term/i
not app: /julia/i
not app: /safari/i
not app: /zoom/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
-

gamepad(dpad_left:down): user.key_hold("left")
gamepad(dpad_left:up): user.key_release("left")
gamepad(dpad_right:down): user.key_hold("right")
gamepad(dpad_right:up): user.key_release("right")
gamepad(dpad_down:down): user.key_hold("down")
gamepad(dpad_down:up): user.key_release("down")
gamepad(dpad_up:down): user.key_hold("up")
gamepad(dpad_up:up): user.key_release("up")

gamepad(north:down): user.key_hold("space")
gamepad(north:up): user.key_release("space")
gamepad(south:down): user.key_hold("enter")
gamepad(south:up): user.key_release("enter")
gamepad(west:down): user.key_hold("backspace")
gamepad(west:up): user.key_release("backspace")
gamepad(east:down): user.key_hold(".")
gamepad(east:up): user.key_release(".")

gamepad(l1): key(ctrl-pageup)
gamepad(r1): key(ctrl-pagedown)

gamepad(l3:down): key(shift:down)
gamepad(l3:up): key(shift:up)

gamepad(r3:down): key(ctrl:down)
gamepad(r3:up): key(ctrl:up)

gamepad(select): key(cmd-w)
gamepad(start): key(cmd-t)


