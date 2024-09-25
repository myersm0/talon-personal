app: /terminal/i
-

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

select to end:
	key(escape)
	key("v")
	key("$")

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
	key(enter)

vim save quit:
	key(escape)
	key(":")
	insert("wq")
	key(enter)

vim quit:
	key(escape)
	key(":")
	key("q")
	key(enter)

vim force quit:
	key(escape)
	key(":")
	key("q")
	key("!")
	key(enter)

vim go:
	key(escape)
	insert(":g/")

vim sub:
	key(escape)
	insert(":%s/")

undo:
	key(escape)
	key("u")

redo:
	key(escape)
	key(ctrl-r)

^(move|tmux) down$:
	key(ctrl-a)
	insert("j")

^(move|tmux) up$:
	key(ctrl-a)
	insert("k")

^(move|tmux) left$:
	key(ctrl-a)
	insert("h")

^(move|tmux) right$:
	key(ctrl-a)
	insert("l")

^[move|tmux] diagonal$:
	key(ctrl-a)
	insert("l")
	key(ctrl-a)
	insert("j")

tmux fullsize:
	key(ctrl-a)
	insert("z")

tmux seek:
	mode.enable("user.seek")
	key(ctrl-a)
	insert("[")

tmux put|paste:
	mode.disable("user.seek")
	key(ctrl-a)
	insert("]")

repl four:
	insert("repl4")
	key(enter)

(lister | list latest):
	insert("ls -ltr")
	key(enter)

listra:
	insert("ls -ltra")
	key(enter)

list:
	insert("ls -l")
	key(enter)

CDM:
	insert("cdm")
	key(enter)

git commit:
	insert("git commit -a -m \"\"")
	key(left)

set minus oh VI:
	insert("set -o vi")
	key(enter)

bash read lines:
	insert("while IFS= read -r line; do")

#bash loop (over|through) files:
#	insert("for file in \"${filelist[@]}\\"; do")

send selection:
	key(f3)

spaces to tabs:
	key(escape)
	insert(":%s/    /\t/g")
	key(enter)

tabs to spaces:
	key(escape)
	insert(":%s/\t/    /g")
	key(enter)

search history:
	insert("history | grep -E ")

(line count|count lines):
	insert("wc -l")

count those lines:
	insert(" | wc -l")

go back$:
	insert("cd ..")
	key(enter)

go home:
	insert("cd")
	key(enter)

^go to$:
	insert("cd ")

go to {user.pathname}:
	insert("cd ")
	insert(pathname)

go ahead:
	insert("goahead -d 1")
	key(enter)

go ahead <digits>:
	insert("goahead -d ")
	insert(digits)
	key(enter)

go ahead <digits> (but|then) wait:
	insert("goahead -d ")
	insert(digits)
	key(space)

go recent$:
	insert("cdr")
	key(enter)

go frequent$:
	insert("cdf")
	key(enter)

go recent (but|then) wait$:
	insert("cdr ")

go frequent (but|then) wait$:
	insert("cdf ")

grep:
	insert("grep -E ")

grep that:
	insert(" | grep -E ")

grep (caseless|insensitive):
	insert("grep -Ei ")

grep recursive:
	insert("grep -Er ")

find:
	insert("find ")

find <digits>:
	insert("find -maxdepth ")
	insert(digits)
	key(space)

copy:
	insert("cp ")

make dir:
	insert("mkdir -p ")

array:
	key(")
	key($)
	key({)
	insert("[@]}")
	key(")
	key(left:5)

squeue:
	insert("squeue")

install:
	insert("sudo apt-get install ")

page that:
	insert(" | less")
	key(enter)





