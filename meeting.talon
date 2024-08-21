
mode: user.meeting
-
^command mode$:
    speech.enable()
    mode.disable("user.meeting")
    mode.enable("command")

key(f5:down):
    speech.enable()

key(f5:up):
    speech.disable()

^toggle mute$:
    key(alt+a)

gamepad(r2):
    key(alt+a)

gamepad(l2:down):
    speech.enable()

gamepad(l2:up):
    speech.disable()



