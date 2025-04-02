
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

