
title: /terminal/i

tiny down:
	key(escape)
	key("j:5")

little down:
	key(escape)
	key("j:10")

big down:
	key(escape)
	key("j:30")

huge down:
	key(escape)
	key("j:100")

tiny up:
	key(escape)
	key("k:5")

little up:
	key(escape)
	key("k:10")

big up:
	key(escape)
	key("k:30")

huge up:
	key(escape)
	key("k:100")

tiny left:
	key(escape)
	key("h:5")

little left:
	key(escape)
	key("h:10")

big left:
	key(escape)
	key("h:30")

huge left:
	key(escape)
	key("h:100")

tiny right:
	key(escape)
	key("l:5")

little right:
	key(escape)
	key("l:10")

big right:
	key(escape)
	key("l:30")

huge right:
	key(escape)
	key("l:100")

change to end:
	key(escape)
	key("c")
	key("$")

change word:
	key(escape)
	key("c")
	key("w")

vim (no|disable) colors:
	key(escape)
	key(":")
	insert("set t_Co=0")
	key(enter)

vim put:
	key(escape)
	key("p")

vim yank <user.number>:
	key(escape)
	n = user.number or 1
	key(n)
	key("y")
	key("y")

vim save:
	key(escape)
	key(":")
	key("w")

vim save quit:
	key(escape)
	key(":")
	insert("wq")

vim quit:
	key(escape)
	key(":")
	key("q")

undo:
	key(escape)
	key("u")

redo:
	key(escape)
	key(ctrl-r)

^down$:
	key(ctrl-a)
	insert("j")

^up$:
	key(ctrl-a)
	insert("k")

^left$:
	key(ctrl-a)
	insert("h")

^right$:
	key(ctrl-a)
	insert("l")

fullsize:
	key(ctrl-a)
	insert("z")

seek:
	key(ctrl-a)
	insert("[")

put|paste:
	key(ctrl-a)
	insert("]")

repl four:
	insert("repl4")
	key(enter)

CD:
	insert("cd ")

go home:
	insert("cd")
	key(enter)

LTR:
	insert("ltr")
	key(enter)

L:
	insert("ls -l")
	key(enter)

git commit:
	insert("git commit -a -m \\"\\"")
	key(left)

set minus oh VI:
	insert("set -o vi")
	key(enter)

bash read lines:
	insert("while IFS= read -r line; do")

bash loop (over|through) files:
	insert("for file in \"${filelist[@]}\"; do")

