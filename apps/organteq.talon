app: /organteq/i
-

^clear {user.organteq_manual}$:
	user.organteq_clear_manual(organteq_manual)

^{user.organteq_manual} <number_small>$:
	user.organteq_toggle_stop(organteq_manual, number_small)

^using {user.organteq_manual}$:
	user.organteq_set_manual(organteq_manual)

^<number_small>$:
	which_manual = user.organteq_get_manual()
	user.organteq_toggle_stop(which_manual, number_small)

