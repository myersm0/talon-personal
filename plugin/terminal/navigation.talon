app: /terminal/i
app: /term/i
-

## navigation helpers 
# (mostly for use with my `Clew.jl` and `bash-productivity` repos)

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

grab$:
	insert("grab")
	key(enter)

grab <digits>$:
	insert("grab -d ")
	insert(digits)
	key(enter)

grab <digits> (but|then) wait:
	insert("grab -d ")
	insert(digits)
	key(space)


