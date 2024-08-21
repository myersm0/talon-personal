from talon import Module, actions, cron

mod = Module()

east_button_held = False
east_button_timer = None
current_char_index = 0
last_char = "."
cycle_chars = [",", "?"]

@mod.action_class
class Actions:
	def handle_east_button_down():
		"""Handles the initial press of the east button"""
		global east_button_held, east_button_timer, current_char_index
		east_button_held = True
		east_button_timer = cron.after("1s", actions.user.east_button_long_press)

	def handle_east_button_up():
		"""Handles the release of the east button"""
		global east_button_held, east_button_timer, last_char, current_char_index
		if east_button_held:
			cron.cancel(east_button_timer)
			# Insert the last character that was cycled to
			actions.insert(last_char)
			east_button_held = False
		current_char_index = 0
		last_char = "."

	def east_button_long_press():
		"""Handles the cycling of characters on a long press"""
		global current_char_index, last_char
		if east_button_held:
			# Update the last character in the cycle but don't insert it yet
			last_char = cycle_chars[current_char_index]
			# Cycle to the next character
			current_char_index = (current_char_index + 1) % len(cycle_chars)
			# Schedule the next character update after a short delay
			cron.after("1s", actions.user.east_button_long_press)

