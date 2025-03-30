app: /terminal/i
app: /term/i
-

unicode {user.unicode}:
	insert(unicode)

[litte] (Greek|unicode) {user.lower_greek}:
	insert(lower_greek)

big (Greek|unicode) {user.upper_greek}:
	insert(upper_greek)

empty args:
	insert("()")

empty brackets:
	insert("[]")


## vim

^look down$:
	user.key_hold("down", 40, "8ms", "0ms")
	sleep(500ms)
	user.key_hold("up", 40, "8ms", "0ms")

^look up$:
	user.key_hold("up", 40, "8ms", "0ms")
	sleep(500ms)
	user.key_hold("down", 40, "8ms", "0ms")

^scroll up$:
	key(escape)
	user.key_hold("up", 256, "8ms", "0ms")

^scroll down$:
	key(escape)
	user.key_hold("down", 256, "8ms", "0ms")

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
	insert(vim_actions)
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

vim go$:
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

^[vim] next$:
	key(escape)
	insert(":n")
	key(enter)

^[vim] previous$:
	key(escape)
	insert(":N")
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


## tmux

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

execute block:
	key(escape)
	key(f12)

execute line:
	key(escape)
	key(0)
	key(v)
	key($)
	key(ctrl-c:2)


## bash 

rsync$:
	insert("rsync -avz ")

rsync from shadow:
	insert("rsync -avz $hpref:")

PB paste:
	insert("$(pbpaste)")

^list [{user.dont_go}]$:
	insert("ls -l")
	go = dont_go or "go"
	user.optional_enter(go)

^(lister|list latest) [{user.dont_go}]:
	insert("ls -ltr")
	go = dont_go or "go"
	user.optional_enter(go)

^listra [{user.dont_go}]:
	insert("ls -ltra")
	go = dont_go or "go"
	user.optional_enter(go)

^list by size [{user.dont_go}]:
	insert("ls -lS")
	go = dont_go or "go"
	user.optional_enter(go)

^list by size reversed [{user.dont_go}]:
	insert("ls -lSr")
	go = dont_go or "go"
	user.optional_enter(go)

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

count those lines [{user.dont_go}]:
	insert(" | wc -l ")
	go = dont_go or "go"
	user.optional_enter(go)

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

grep {user.grep_options}+:
	insert("grep -E")
	insert(user.concatenate(grep_options_list))
	insert(" ")

streaming editor:
	insert("sed -E ")

# pipe, redirect, or append
{user.unix_operators} that [to {user.unix_tools}]:
	key(space)
	insert(unix_operators)
	key(space)
	insert(unix_tools)

find [{user.dont_go}]$:
	insert("find .")
	go = dont_go or "go"
	user.optional_enter(go)

find <digits> [{user.dont_go}]:
	insert("find . -maxdepth ")
	insert(digits)
	go = dont_go or "go"
	user.optional_enter(go)

copy:
	insert("cp ")

copy recusrive:
	insert("cp -r ")

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

page that [{user.dont_go}]:
	insert(" | less")
	go = dont_go or "go"
	user.optional_enter(go)

julia main [{user.dont_go}]:
	insert("julia main.jl")
	go = dont_go or "go"
	user.optional_enter(go)

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

go to {user.pathnames}:
	insert("cd ")
	insert(pathnames)
	key(enter)

go ahead$:
	insert("goahead -d 1")
	key(enter)

go ahead <digits> [{user.dont_go}]$:
	insert("goahead -d ")
	insert(digits)
	go = dont_go or "go"
	user.optional_enter(go)

go recent [{user.dont_go}]$:
	insert("cdr")
	go = dont_go or "go"
	user.optional_enter(go)

go frequent [{user.dont_go}]$:
	insert("cdf")
	go = dont_go or "go"
	user.optional_enter(go)

grab$:
	insert("grab")
	key(enter)

grab <digits>$ [{user.dont_go}]:
	insert("grab -d ")
	insert(digits)
	go = dont_go or "go"
	user.optional_enter(go)

^<number> snap$:
	insert(number)
	key(enter)

^snap <number>$:
	insert(number)
	key(enter)


## for use with my personal note taker

log read <phrase> [{user.dont_go}]:
	insert("~/contents/101804/read.sh -c ")
	insert(phrase)
	go = dont_go or "go"
	user.optional_enter(go)

log write <phrase>:
	insert("log ")
	insert(phrase)
	key(enter)


## Google Gemma

^fim prefix$: insert("<|fim_prefix|>")
^fim middle$: insert("<|fim_middle|>")
^fim suffix$: insert("<|fim_suffix|>")



