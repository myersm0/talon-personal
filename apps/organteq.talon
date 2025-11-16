app: /organteq/i
-

## managing stops and manuals

^clear {user.organteq_manual}$:
	user.organteq_clear_manual(organteq_manual)

^{user.organteq_manual} {user.organteq_stop_number}+$:
	user.organteq_toggle_stops(organteq_manual, organteq_stop_number_list)

^(with|use|using) {user.organteq_manual}$:
	user.organteq_set_manual(organteq_manual)

^{user.organteq_stop_number}+$:
	which_manual = user.organteq_get_manual()
	user.organteq_toggle_stops(which_manual, organteq_stop_number_list)


## accessing settings panels

^settings$:
	key(u)

^stops$:
	key(s)

^tremulants$:
	key(t)



