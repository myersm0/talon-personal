app: /terminal/i
app: /term/i
-


## vim

vim (no|disable) colors:
	key(escape)
	key(":")
	insert("set t_Co=0")
	key(enter)

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

vim put:
	key(escape)
	key("p")

vim yank <digits>:
	key(escape)
	n = digits or 1
	insert(n)
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

vim next:
	key(escape)
	insert(":n")
	key(enter)

vim command:
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


## tmux

^[move|tmux] down$:
	key(ctrl-a)
	insert("j")

^[move|tmux] up$:
	key(ctrl-a)
	insert("k")

^[move|tmux] left$:
	key(ctrl-a)
	insert("h")

^[move|tmux] right$:
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

four across:
	insert("four_across")
	key(enter)


## bash 

list$:
	insert("ls -l")
	key(enter)

(lister|list latest):
	insert("ls -ltr")
	key(enter)

listra:
	insert("ls -ltra")
	key(enter)

list by size:
	insert("ls -lS")
	key(enter)

list by size reversed:
	insert("ls -lSr")
	key(enter)

git commit:
	insert("git commit -a -m \"\"")
	key(left)

set minus oh VI:
	insert("set -o vi")
	key(enter)

read lines [(as|into) <phrase>]:
	var = phrase or "line"
	insert("while IFS= read -r ")
	insert(var)
	insert("; do")

for <phrase> in {user.array_names}:
	insert("for ")
	insert(phrase)
	insert(" in ")
	key(")
	key($)
	key({)
	insert(array_names)
	insert("[@]}")
	key(")
	insert("; do")

search history:
	insert("history | grep -Ei ")

(line count|count lines):
	insert("wc -l ")

count those lines:
	insert(" | wc -l ")

go back$:
	insert("cd ..")
	key(enter)

go home:
	insert("cd")
	key(enter)

^go to$:
	insert("cd ")

grep:
	insert("grep -E ")

grep that:
	insert(" | grep -E ")

# todo: make a dictionary of grep options to use as captures
grep (caseless|insensitive):
	insert("grep -Ei ")

grep recursive:
	insert("grep -Er ")

grep recursive insensitive:
	insert("grep -Eri ")

find$:
	insert("find . ")

find <digits>:
	insert("find . -maxdepth ")
	insert(digits)
	key(space)

copy:
	insert("cp ")

make (folder|dir):
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

page that:
	insert(" | less")
	key(enter)

julia main:
	insert("julia main.jl ")

cmus:
	insert("cmus")

cmus remote:
	insert("cmus-remote ")


## navigation helpers (for use with my `Clew.jl` and `bash-productivity` repos)

clew (insert|create):
	insert("clew insert ")
	key(":2)
	key(left)

clew (find|search)$:
	insert("clew search --data=")
	key(":2)
	key(left)

clew (find|search) from current$:
	insert("clew search --data=.")
	key(enter)

go to {user.pathname}:
	insert("cd ")
	insert(pathname)
	key(enter)

go ahead$:
	insert("goahead -d 1")
	key(enter)

go ahead <digits>$:
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

go recent (but|then) wait:
	insert("cdr ")

go frequent (but|then) wait:
	insert("cdf ")


## for use with my personal note taker

log read <phrase>:
	insert("log read ")
	insert(phrase)
	key(enter)

log write <phrase>:
	insert("log ")
	insert(phrase)
	key(enter)

