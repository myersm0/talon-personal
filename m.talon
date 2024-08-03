select everything:
	key(cmd-a)

change to end:
	key("c")
	key("$")

change word:
	key("c")
	key("w")

vim (no|disable) colors:
	key(":")
	insert("set t_Co=0")
	key(enter)

vim put:
	key("p")

vim yank:
	key("y")
	key("y")

vim save:
	key(":")
	key("w")

vim save quit:
	key(":")
	insert("wq")

vim quit:
	key(":")
	key("q")

vim undo:
	key("u")

vim redo:
	key(ctrl-r)

tmux down:
	key(ctrl-a)
	insert("j")

tmux up:
	key(ctrl-a)
	insert("k")

tmux left:
	key(ctrl-a)
	insert("h")

tmux right:
	key(ctrl-a)
	insert("l")

tmux fullsize:
	key(ctrl-a)
	insert("z")

tmux seek:
	key(ctrl-a)
	insert("[")

tmux paste:
	key(ctrl-a)
	insert("]")

key(ctrl-e):
	tracking.control_toggle()

repl four:
	insert("repl4")
	key(enter)

bash CD:
	insert("cd ")

bash LTR:
	insert("ltr")
	key(enter)

bash L:
	insert("ls -l ")



