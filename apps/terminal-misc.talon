app: /term*/i

-

unicode {user.unicode}:
	insert(unicode)

[lower|little] (Greek|unicode) {user.lower_greek}:
	insert(lower_greek)

(upper|big) (Greek|unicode) {user.upper_greek}:
	insert(upper_greek)

empty args:
	insert("()")

empty brackets:
	insert("[]")

serve piano tech:
	insert("/Applications/Pianoteq\ 9/Pianoteq\ 9.app/Contents/MacOS/Pianoteq\ 9 --serve ")
	key(enter)

serve organ tech:
	insert("/Applications/Organteq\ 2/Organteq\ 2.app/Contents/MacOS/Organteq\ 2 --serve ")
	key(enter)

oh lama serve:
	insert("ollama serve")
	key(enter)


