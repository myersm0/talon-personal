
^meeting mode$:
    mode.enable("user.meeting")
    speech.disable()

select everything:
	key(cmd-a)

key(ctrl-e):
	tracking.control_toggle()

service account:
	insert("nrg-svc-hcpi")

backspace:
	key(bksp)

workspace (right|next):
	key(ctrl-alt-right)
	
workspace (left|previous):
	key(ctrl-alt-left)

path desdemona:
	insert("/media/m/desdemona/contents/")

path daphne:
	insert("/media/m/daphne/contents/")

path diomedes:
	insert("/media/m/diomedes/contents/")

key(f6:down):
	speech.disable()

key(f6:up):
	speech.enable()

key(f7):
	speech.toggle()

take context:
    key(f8)

take screenshot:
    key(f9)

(take note | note to self):
    key(f10)


