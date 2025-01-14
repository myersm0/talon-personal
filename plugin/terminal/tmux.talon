app: /terminal/i
app: /term/i
-

^[go|move|tmux] down$:
	key(ctrl-a)
	insert("j")

^[go|move|tmux] up$:
	key(ctrl-a)
	insert("k")

^[go|move|tmux] left$:
	key(ctrl-a)
	insert("h")

^[go|move|tmux] right$:
	key(ctrl-a)
	insert("l")

^[go|move|tmux] diagonal$:
	key(ctrl-a)
	insert("l")
	key(ctrl-a)
	insert("j")

[tmux] fullsize:
	key(ctrl-a)
	insert("z")

[tmux] seek:
	mode.enable("user.seek")
	key(ctrl-a)
	insert("[")

[tmux] put|paste:
	mode.disable("user.seek")
	key(ctrl-a)
	insert("]")

repl four:
	insert("repl4")
	key(enter)

four across:
	insert("four_across")
	key(enter)


