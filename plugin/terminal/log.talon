app: /terminal/i
app: /term/i
-

## for use with my personal note taker

log read <phrase>:
	insert("log read ")
	insert(phrase)
	key(enter)

log write <phrase>:
	insert("log ")
	insert(phrase)
	key(enter)

