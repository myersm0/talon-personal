app: /terminal/i
-

clew (find|search)$:
	insert("clew search --data=")
	key(":2)
	key(left)

clew (find|search) from current$:
	insert("clew search --data=.")
	key(enter)

clew (insert|create):
	insert("clew insert --base_dir=~/contents --purpose=")
	key(":2)
	key(left)



