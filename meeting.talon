
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

gamepad(m2:down):
    speech.enable()

gamepad(m2:up):
    speech.disable()



