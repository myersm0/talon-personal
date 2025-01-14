app: /terminal/i
app: /term/i
-

rsync$:
	insert("rsync -avz ")

rsync from shadow:
	insert("rsync -avz $hpref:")

PB paste:
	insert("$(pbpaste)")

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

grep {user.grep_options}+:
	insert("grep -E")
	insert(user.concatenate(grep_options_list))
	insert(" ")

sed:
	insert("sed -E ")

sed that:
	insert(" | sed -E ")

[pipe|pass] that to {user.unix_tools}:
	insert(" | ")
	insert(unix_tools)

find$:
	insert("find . ")

find <digits>:
	insert("find . -maxdepth ")
	insert(digits)
	key(space)

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

page that:
	insert(" | less")
	key(enter)

julia main:
	insert("julia main.jl ")

cmus:
	insert("cmus")

cmus remote:
	insert("cmus-remote ")


