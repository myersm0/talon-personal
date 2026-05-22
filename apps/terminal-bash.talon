app: /term*/i

-

tag(): user.use_app_git

go to {user.pathnames}:
	insert("cd ")
	insert(pathnames)
	key(enter)

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

copy recursive:
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

victor chase:
	insert("vim ")


