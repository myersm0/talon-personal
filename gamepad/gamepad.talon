mode: command
mode: dictation
mode: sleep
mode: user.quiet
tag: user.my_overrides
-

# keys sent by the InputConfig preset; sticks, triggers and PS never reach Talon

key(f13:down):        user.gamepad_button_down("dpad_left")
key(f13:up):          user.gamepad_button_up("dpad_left")
key(f14:down):        user.gamepad_button_down("dpad_up")
key(f14:up):          user.gamepad_button_up("dpad_up")
key(f15:down):        user.gamepad_button_down("dpad_right")
key(f15:up):          user.gamepad_button_up("dpad_right")
key(f16:down):        user.gamepad_button_down("dpad_down")
key(f16:up):          user.gamepad_button_up("dpad_down")

key(f17:down):        user.gamepad_button_down("west")
key(f17:up):          user.gamepad_button_up("west")
key(f18:down):        user.gamepad_button_down("north")
key(f18:up):          user.gamepad_button_up("north")
key(f19:down):        user.gamepad_button_down("east")
key(f19:up):          user.gamepad_button_up("east")
key(f20:down):        user.gamepad_button_down("south")
key(f20:up):          user.gamepad_button_up("south")

key(shift-f13:down):  user.gamepad_button_down("select")
key(shift-f13:up):    user.gamepad_button_up("select")
key(shift-f14:down):  user.gamepad_button_down("start")
key(shift-f14:up):    user.gamepad_button_up("start")

key(shift-f15:down):  user.gamepad_button_down("left_shoulder")
key(shift-f15:up):    user.gamepad_button_up("left_shoulder")
key(shift-f16:down):  user.gamepad_button_down("right_shoulder")
key(shift-f16:up):    user.gamepad_button_up("right_shoulder")

key(shift-f17:down):  user.gamepad_button_down("left_paddle")
key(shift-f17:up):    user.gamepad_button_up("left_paddle")
key(shift-f18:down):  user.gamepad_button_down("right_paddle")
key(shift-f18:up):    user.gamepad_button_up("right_paddle")

key(shift-f19:down):  user.gamepad_button_down("left_function")
key(shift-f19:up):    user.gamepad_button_up("left_function")
key(shift-f20:down):  user.gamepad_button_down("right_function")
key(shift-f20:up):    user.gamepad_button_up("right_function")
