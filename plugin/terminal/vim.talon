app: /terminal/i
app: /term/i
-

[vim] (no|disable) colors:
	key(escape)
	key(":")
	insert("set t_Co=0")
	key(enter)

{user.vim_actions} word:
	key(escape)
	insert(vim_actions)
	key("w")

{user.vim_actions} <digits> words:
	key(escape)
	insert(digits)
	insert(vim_actions)
	key("w")

{user.vim_actions} to end:
	key(escape)
	insert(digits)
	key("$")

{user.vim_actions} line:
	key(escape)
	insert(vim_actions)
	insert(vim_actions)

{user.vim_actions} <digits> lines:
	key(escape)
	insert(digits)
	insert(vim_actions)
	insert(vim_actions)

[vim] put:
	key(escape)
	key("p")

[vim] save:
	key(escape)
	key(":")
	key("w")
	key(enter)

[vim] save quit:
	key(escape)
	key(":")
	insert("wq")
	key(enter)

[vim] quit:
	key(escape)
	key(":")
	key("q")
	key(enter)

[vim] force quit:
	key(escape)
	key(":")
	key("q")
	key("!")
	key(enter)

[vim] go$:
	key(escape)
	insert(":g/")

[vim] sub$:
	key(escape)
	insert(":%s/")

[vim] sub from <digits> to <digits>:
	key(escape)
	key(:)
	insert(digits_1)
	key(,)
	insert(digits_2)
	insert("s/")

[vim] sub from <digits>[ to end]:
	key(escape)
	key(:)
	insert(digits_1)
	key(,)
	insert("$s/")

[vim] next$:
	key(escape)
	insert(":n")
	key(enter)

[vim] command$:
	key(escape)
	key(:)
	key(!)

undo:
	key(escape)
	key("u")

redo:
	key(escape)
	key(ctrl-r)

spaces to tabs:
	key(escape)
	insert(":%s/    /\t/g")
	key(enter)

tabs to spaces:
	key(escape)
	insert(":%s/\t/    /g")
	key(enter)


