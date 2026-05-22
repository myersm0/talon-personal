app: /term*/i

-

^[go|move|tmux] (down|south)$:
	key(ctrl-j)

^[go|move|tmux] (up|north)$:
	key(ctrl-k)

^[go|move|tmux] (left|west)$:
	key(ctrl-h)

^[go|move|tmux] (right|east)$:
	key(ctrl-l)

^[go|move|tmux] southeast$:
	key(ctrl-j)
	key(ctrl-l)

^[go|move|tmux] southwest$:
	key(ctrl-j)
	key(ctrl-h)

^[go|move|tmux] northwest$:
	key(ctrl-k)
	key(ctrl-h)

^[go|move|tmux] northeast$:
	key(ctrl-k)
	key(ctrl-l)

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


