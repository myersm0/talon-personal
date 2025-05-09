
^stop$:
	user.release_all_keys()

^meeting mode$:
	mode.enable("user.meeting")
	user.set_default_mic()
	speech.disable()

^symbol mode$:
	mode.enable("user.symbol")

^long mode$:
	mode.enable("user.long")

^done with long mode$:
	mode.disable("user.long")

^done with seeking$:
	 key(q)

^done with symbols$:
	mode.disable("user.symbol")

^done with mouse$:
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
	key(ctrl-right)
	
workspace (left|previous):
	key(ctrl-left)

window next:
	key(cmd-`)

key(f6:down):
	speech.disable()

key(f6:up):
	speech.enable()

key(f7):
	speech.toggle()

take screenshot:
	user.take_screenshot()

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

(comma|Komma|item):
	key(,)
	key(space)

networking (on|enable):
	user.networking_on()

networking (off|disable):
	user.networking_off()

(funk eleven|full screen):
	key(f11)

maximize:
	key(alt-f10)

^crunch$:
	key(ctrl-c)

divide:
	key(/)

^(selection clip|clip this)$:
	user.save_selected_text_to_file()

^(microphone|microphones|set (default|normal|favorite|preferred) Mike)$:
	user.set_default_mic()

^[set] (builtin|dummy) Mike$:
	user.set_builtin_mic()



