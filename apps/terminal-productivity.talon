app: /term*/i

-

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

go likely [{user.dont_go}]$:
	insert("cdp")
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

^recall [{user.dont_go}]$:
	insert("recall")
	go = dont_go or "go"
	user.optional_enter(go)

^recall minus pee [{user.dont_go}]$:
	insert("recall -p ")
	go = dont_go or "go"
	user.optional_enter(go)


