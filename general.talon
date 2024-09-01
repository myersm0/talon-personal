
^meeting mode$:
    mode.enable("user.meeting")
    speech.disable()

^symbol mode$:
    mode.enable("user.symbol")

done with seeking:
	 key(q)

done with symbols:
    mode.disable("user.symbol")

done with mouse:
    mode.disable("user.mouse")

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

surround <user.symbol_key>:
	key(" ")
	key(symbol_key)
	key(" ")

surround <user.letter>:
	key(" ")
	key(letter)
	key(" ")

double <user.symbol_key>:
	key(symbol_key)
	key(symbol_key)

quote:
	key(")

Komma:
	key(,)





