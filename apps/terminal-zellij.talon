app: /term*/i

-

^[go|move|tmux] (down|south)$:
	key(ctrl-p)
	key(down)
	key(enter)

^[go|move|tmux] (up|north)$:
	key(ctrl-p)
	key(up)
	key(enter)

^[go|move|tmux] (left|west)$:
	key(ctrl-p)
	key(left)
	key(enter)

^[go|move|tmux] (right|east)$:
	key(ctrl-p)
	key(right)
	key(enter)

^[go|move|tmux] southeast$:
	key(ctrl-p)
	key(down)
	key(right)
	key(enter)

^[go|move|tmux] southwest$:
	key(ctrl-p)
	key(down)
	key(left)
	key(enter)

^[go|move|tmux] northwest$:
	key(ctrl-p)
	key(up)
	key(left)
	key(enter)

^[go|move|tmux] northeast$:
	key(ctrl-p)
	key(up)
	key(right)
	key(enter)

^(shock | execute block)$:
	key(escape)
	insert("gb")

^(shine | execute line)$:
	key(escape)
	key(0)
	key(V)
	insert("gs")

^float$:
	key(ctrl-shift-f)

^new pane$:
	key(ctrl-p)
	key(n)

^new pane right$:
	key(ctrl-p)
	key(r)

^new pane down$:
	key(ctrl-p)
	key(d)

^stack$:
	key(ctrl-p)
	key(s)

^eject$:
	key(ctrl-p)
	key(e)

^tab rename$:
	key(ctrl-t)
	key(r)


