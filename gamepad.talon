app: firefox
app: gedit
app: xed
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
gamepad(west:down): key(backspace)
gamepad(east:down): key(".")

gamepad(east:down):
    user.handle_east_button_down()

gamepad(east:up):
    user.handle_east_button_up()

