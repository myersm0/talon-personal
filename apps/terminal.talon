app: /terminal/i
app: /term/i
-

## work project names
CCF {user.project} {user.project_qualifier}:
	insert("CCF_")
	insert(project)
	insert("_")
	insert(project_qualifier)


## slurm
cue stat [{user.dont_go}]: 
	insert('squeue -u $USER -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"')
	go = dont_go or "go"
	user.optional_enter(go)

cue stat HCP:
	insert('squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R" | grep HCP')
	go = dont_go or "go"
	user.optional_enter(go)

cue stat ADCP:
	insert('squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R" | grep ADCP')
	go = dont_go or "go"
	user.optional_enter(go)



## misc
unicode {user.unicode}:
	insert(unicode)

[lower|litte] (Greek|unicode) {user.lower_greek}:
	insert(lower_greek)

(upper|big) (Greek|unicode) {user.upper_greek}:
	insert(upper_greek)

empty args:
	insert("()")

empty brackets:
	insert("[]")


## vim

# some nonsense to clear the highlighted strings matching my last "go" cmd
vim clear:
	key(escape)
	insert(":g/fetneantefnenao")
	key(enter)

set number:
	key(escape)
	insert(":set number")
	key(enter)

set no number:
	key(escape)
	insert(":set nonumber")
	key(enter)

victor chase:
	insert("vim ")

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

^[vim] (no|disable) colors$:
	key(escape)
	key(":")
	insert("set t_Co=0")
	key(enter)

^{user.vim_actions} word$:
	key(escape)
	insert(vim_actions)
	key("w")

^{user.vim_actions} <digits> words$:
	key(escape)
	insert(digits)
	insert(vim_actions)
	key("w")

^{user.vim_actions} to end$:
	key(escape)
	insert(vim_actions)
	key("$")

^{user.vim_actions} line$:
	key(escape)
	insert(vim_actions)
	insert(vim_actions)

^{user.vim_actions} <digits> lines$:
	key(escape)
	insert(digits)
	insert(vim_actions)
	insert(vim_actions)

^[vim] put$:
	key(escape)
	key("p")

^[vim] save$:
	key(escape)
	key(":")
	key("w")
	key(enter)

^[vim] save quit$:
	key(escape)
	key(":")
	insert("wq")
	key(enter)

^[vim] quit$:
	key(escape)
	key(":")
	key("q")
	key(enter)

^[vim] force quit$:
	key(escape)
	key(":")
	key("q")
	key("!")
	key(enter)

^vim go$:
	key(escape)
	insert(":g/")

^[vim] sub$:
	key(escape)
	insert(":%s/")

^[vim] next$:
	key(escape)
	insert(":n")
	key(enter)

^[vim] previous$:
	key(escape)
	insert(":N")
	key(enter)

^vim command$:
	key(escape)
	key(:)
	key(!)

^undo$:
	key(escape)
	key("u")

^redo$:
	key(escape)
	key(ctrl-r)

^spaces to tabs$:
	key(escape)
	insert(":%s/    /\t/g")
	key(enter)

^tabs to spaces$:
	key(escape)
	insert(":%s/\t/    /g")
	key(enter)

^[vim] sub from <digits> to <digits>$:
	key(escape)
	key(:)
	insert(digits_1)
	key(,)
	insert(digits_2)
	insert("s/")

^[vim] sub from <digits> [to end]$:
	key(escape)
	key(:)
	insert(digits_1)
	key(,)
	insert("$s/")

^[vim] {user.vim_actions_long} from <digits> to <digits>$:
	key(escape)
	key(:)
	insert(digits_1)
	key(,)
	insert(digits_2)
	insert(vim_actions_long)
	key(enter)

^[vim] {user.vim_actions_long} from <digits> [to end]$:
	key(escape)
	key(:)
	insert(digits_1)
	key(,)
	key($)
	insert(vim_actions_long)
	key(enter)

^[vim] {user.vim_actions_long} <digits>$:
	key(escape)
	key(:)
	insert(digits)
	insert(vim_actions_long)
	key(enter)

^[vim] put at <digits>:
	key(escape)
	key(:)
	insert(digits_1)
	insert("put")
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

^[go|move|tmux] (diagonal|oblique|cross)$:
	key(ctrl-a)
	key(left)
	sleep(10ms)
	key(ctrl-a)
	key(up)

^[tmux] fullsize$:
	key(ctrl-a)
	insert("z")

^[tmux] seek$:
	mode.enable("user.seek")
	key(ctrl-a)
	insert("[")

^[tmux] put|paste$:
	mode.disable("user.seek")
	key(ctrl-a)
	insert("]")

^repl four$:
	insert("repl4")
	key(enter)

^four across$:
	insert("four_across")
	key(enter)

^(shock | execute block)$:
	key(escape)
	key(f12)

^(shine | execute line)$:
	key(escape)
	key(0)
	key(v)
	key($)
	key(ctrl-c:2)


## bash 

rsync$:
	insert("rsync -avz ")

rsync from chpc$:
	insert("rsync -avz $cpref:")

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

go to:
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

page that [{user.dont_go}]:
	insert(" | less")
	go = dont_go or "go"
	user.optional_enter(go)

cmus:
	insert("cmus")

cmus remote:
	insert("cmus-remote ")

julia main [{user.dont_go}]:
	insert("julia main.jl")
	go = dont_go or "go"
	user.optional_enter(go)

julia go [{user.dont_go}]:
	insert("julia go.jl")
	go = dont_go or "go"
	user.optional_enter(go)

python main [{user.dont_go}]:
	insert("python main.py")
	go = dont_go or "go"
	user.optional_enter(go)

python go [{user.dont_go}]:
	insert("python go.py")
	go = dont_go or "go"
	user.optional_enter(go)

conda activate:
	insert("conda activate ")

conda deactivate:
	insert("conda deactivate")
	key(enter)

^module load$:
	insert("module load ")


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

go to comlogs$:
	insert("goahead -d 5 -r comlogs")
	key(enter)

go to runlogs$:
	insert("goahead -d 5 -r runlogs")
	key(enter)

go ahead <digits> [{user.dont_go}]$:
	insert("goahead -d ")
	insert(digits)
	go = dont_go or "go"
	user.optional_enter(go)

go behind$:
	insert("gobehind")
	key(enter)

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

^<digits> snap$:
	insert(digits)
	key(enter)

^snap <digits>$:
	insert(digits)
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


## ssh

^chpc$:
	insert("ssh login3.chpc.wustl.edu -l michael.myers -X")
	key(enter)

^chpc as service user$:
	insert("ssh -X nrg-svc-hcpi@10.27.136.151")
	key(enter)

^shadow <number>$:
	insert("ssh hcpi-shadow")
	insert(number)
	insert(".nrg.wustl.edu -l michael.myers -X")
	key(enter)

^shadow <number> as service user$:
	insert("ssh hcpi-shadow")
	insert(number)
	insert(".nrg.wustl.edu -l nrg-svc-hcpi -X")
	key(enter)

^brain mappers$:
	insert("ssh brainmappers@brainmappers-desktop5.wustl.edu")
	key(enter)







