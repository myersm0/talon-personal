from talon import Module, Context, actions, ui, ctrl, cron
from talon.screen import Screen
import time

hold_timeout1 = 0.3
hold_timeout2 = 0.8

screen: Screen = ui.main_screen()
mod = Module()
slow_scroll = False
slow_mouse_move = False
timestamps = {}
scheduled_actions = {}

buttons_with_autorelease = (
	"north", "south", "west", "east",
	"start", "select",
	"left_shoulder", "right_shoulder"
)

need_to_go_back_to_sleep = False

@mod.action_class
class Actions:
	# DPAD buttons

	def gamepad_press_dpad_left():
		"""Gamepad press button dpad left"""
		gamepad_mouse_jump("left")

	def gamepad_release_dpad_left(held: int):
		"""Gamepad release button dpad left"""
		actions.skip()

	def gamepad_press_dpad_up():
		"""Gamepad press button dpad up"""
		gamepad_mouse_jump("up")

	def gamepad_release_dpad_up(held: int):
		"""Gamepad release button dpad up"""
		actions.skip()

	def gamepad_press_dpad_right():
		"""Gamepad press button dpad right"""
		gamepad_mouse_jump("right")

	def gamepad_release_dpad_right(held: int):
		"""Gamepad release button dpad right"""
		actions.skip()

	def gamepad_press_dpad_down():
		"""Gamepad press button dpad down"""
		gamepad_mouse_jump("down")

	def gamepad_release_dpad_down(held: int):
		"""Gamepad release button dpad down"""
		actions.skip()

	# Compass / ABXY buttons

	def gamepad_press_west():
		"""Gamepad press button west"""
		actions.mouse_drag(0)

	def gamepad_release_west(held: int):
		"""Gamepad release button west"""
		actions.mouse_release(0)

	def gamepad_press_north():
		"""Gamepad press button north"""
		actions.mouse_drag(1)

	def gamepad_release_north(held: int):
		"""Gamepad release button north"""
		actions.mouse_release(1)

	def gamepad_press_east():
		"""Gamepad press button east"""
		actions.user.mouse_click("control")

	def gamepad_release_east(held: int):
		"""Gamepad release button east"""
		actions.skip()

	def gamepad_press_south():
		"""Gamepad press button south"""
		actions.user.mouse_freeze_toggle()

	def gamepad_release_south(held: int):
		"""Gamepad release button south"""
		if held:
			actions.user.mouse_freeze_toggle()

	# Select / Start buttons

	def gamepad_press_select():
		"""Gamepad press button select"""
		actions.user.quick_pick_show()

	def gamepad_release_select(held: int):
		"""Gamepad release button select"""
		actions.skip()

	def gamepad_press_start():
		"""Gamepad press button start"""
		actions.skip()

	def gamepad_release_start(held: int):
		"""Gamepad release button start"""
		actions.skip()

	# Shoulder buttons

	def gamepad_press_left_shoulder():
		"""Gamepad press button left shoulder"""
		actions.user.go_back()

	def gamepad_release_left_shoulder(held: int):
		"""Gamepad release button left shoulder"""
		actions.skip()

	def gamepad_press_right_shoulder():
		"""Gamepad press button right shoulder"""
		actions.user.go_forward()

	def gamepad_release_right_shoulder(held: int):
		"""Gamepad release button right shoulder"""
		actions.skip()

	# Stick buttons

	def gamepad_press_left_stick():
		"""Gamepad press button left thumb stick"""
		global need_to_go_back_to_sleep
		if not actions.speech.enabled():
			actions.speech.enable()
			need_to_go_back_to_sleep = True
		actions.mimic("long mode")

	def gamepad_release_left_stick(held: int):
		"""Gamepad release button left thumb stick"""
		global need_to_go_back_to_sleep
		actions.mimic("done with long mode")
		if need_to_go_back_to_sleep:
			actions.speech.disable()
			need_to_go_back_to_sleep = False

	def gamepad_press_right_stick():
		"""Gamepad press button right thumb stick"""
		actions.mimic("dictation mode")

	def gamepad_release_right_stick(held: int):
		"""Gamepad release button right thumb stick"""
		actions.mimic("command mode")

	# Analog triggers

	def gamepad_trigger_left(value: float):
		"""Gamepad trigger left movement"""
		gamepad_scroll(0, value * -1.5)

	def gamepad_trigger_right(value: float):
		"""Gamepad trigger right movement"""
		gamepad_scroll(0, value * 1.5)

	# Analog thumb sticks

	def gamepad_stick_left(x: float, y: float):
		"""Gamepad left stick movement"""
		gamepad_scroll(x, y)

	def gamepad_stick_right(x: float, y: float):
		"""Gamepad right stick movement"""
		gamepad_mouse_move(x, y)

	# Scaffolding actions used by the Talon file

	def gamepad_action_dispatch(button: str, held: int):
		"""temp"""
		match button:
			case "dpad_left":
				actions.user.gamepad_release_dpad_left(held)
			case "dpad_up":
				actions.user.gamepad_release_dpad_up(held)
			case "dpad_right":
				actions.user.gamepad_release_dpad_right(held)
			case "dpad_down":
				actions.user.gamepad_release_dpad_down(held)
			case "west":
				actions.user.gamepad_release_west(held)
			case "north":
				actions.user.gamepad_release_north(held)
			case "east":
				actions.user.gamepad_release_east(held)
			case "south":
				actions.user.gamepad_release_south(held)
			case "select":
				actions.user.gamepad_release_select(held)
			case "start":
				actions.user.gamepad_release_start(held)
			case "left_shoulder":
				actions.user.gamepad_release_left_shoulder(held)
			case "right_shoulder":
				actions.user.gamepad_release_right_shoulder(held)
			case "left_stick":
				actions.user.gamepad_release_left_stick(held)
			case "right_stick":
				actions.user.gamepad_release_right_stick(held)
			case _:
				raise ValueError(f"Unknown button: {button}")

	def gamepad_button_down(button: str):
		"""Gamepad press button <button>"""
		timestamps[button] = time.perf_counter()
		if button in buttons_with_autorelease:
			scheduled_actions[button] = cron.after(
				"800ms", 
				lambda: actions.user.gamepad_action_dispatch(button, 2)
			)
		match button:
			case "dpad_left":
				actions.user.gamepad_press_dpad_left()
			case "dpad_up":
				actions.user.gamepad_press_dpad_up()
			case "dpad_right":
				actions.user.gamepad_press_dpad_right()
			case "dpad_down":
				actions.user.gamepad_press_dpad_down()
			case "west":
				actions.user.gamepad_press_west()
			case "north":
				actions.user.gamepad_press_north()
			case "east":
				actions.user.gamepad_press_east()
			case "south":
				actions.user.gamepad_press_south()
			case "select":
				actions.user.gamepad_press_select()
			case "start":
				actions.user.gamepad_press_start()
			case "left_shoulder":
				actions.user.gamepad_press_left_shoulder()
			case "right_shoulder":
				actions.user.gamepad_press_right_shoulder()
			case "left_stick":
				actions.user.gamepad_press_left_stick()
			case "right_stick":
				actions.user.gamepad_press_right_stick()
			case _:
				raise ValueError(f"Unknown button: {button}")

	def gamepad_button_up(button: str):
		"""Gamepad release button <button>"""
		duration = time.perf_counter() - timestamps[button]
		if duration > hold_timeout2:
			held = 2
		elif duration > hold_timeout1:
			held = 1
		else:
			held = 0
		if button in buttons_with_autorelease:
			job = scheduled_actions[button]
			cron.cancel(job)
			expiration_time = job.expiry
			now = cron.time.perf_counter()
			if now >= expiration_time:
				return
		actions.user.gamepad_action_dispatch(button, held)

def gamepad_scroll(x: float, y: float):
	"""Perform gamepad scrolling"""
	multiplier = 1.5 if slow_scroll else 3
	x = x**3 * multiplier
	y = y**3 * multiplier

	if x != 0 or y != 0:
		actions.mouse_scroll(x=x, y=y, by_lines=True)


def gamepad_mouse_move(dx: float, dy: float):
	"""Perform gamepad mouse cursor movement"""
	multiplier = 0.1 if slow_mouse_move else 0.2
	x, y = ctrl.mouse_pos()
	screen = get_screen(x, y)
	dx = dx**3 * screen.dpi * multiplier
	dy = dy**3 * screen.dpi * multiplier
	actions.mouse_move(x + dx, y + dy)


def gamepad_scroll_slow_toggle():
	"""Toggle gamepad slow scroll mode"""
	global slow_scroll
	slow_scroll = not slow_scroll
	# actions.user.notify(f"Gamepad slow scroll: {slow_scroll}")


def gamepad_mouse_move_slow_toggle():
	"""Toggle gamepad slow mouse move mode"""
	global slow_mouse_move
	slow_mouse_move = not slow_mouse_move
	# actions.user.notify(f"Gamepad slow move: {slow_move}")


def gamepad_mouse_jump(direction: str):
	"""Move the mouse cursor to the specified quadrant of the active screen"""
	x, y = ctrl.mouse_pos()
	rect = ui.screen_containing(x, y).rect

	# Half distance between cursor and screen edge
	match direction:
		case "up":
			y = rect.top + (y - rect.top) / 2
		case "down":
			y = rect.bot - (rect.bot - y) / 2
		case "left":
			x = rect.left + (x - rect.left) / 2
		case "right":
			x = rect.right - (rect.right - x) / 2

	actions.mouse_move(x, y)


def get_screen(x: float, y: float) -> Screen:
	global screen
	if not screen.contains(x, y):
		screen = ui.screen_containing(x, y)
	return screen

