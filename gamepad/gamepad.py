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
trigger_jobs = {}

buttons_with_autorelease = (
	"north", "south", "west", "east",
	"start", "select",
	"left_shoulder", "right_shoulder",
)

need_to_go_back_to_sleep = False
stick_holding = None  # track which stick is currently held: 'left', 'right', or None
allow_autorelease = True

mouse_mode_expiration = None
def initiate_mouse_mode(duration: str = "3s"):
	"""temp"""
	global mouse_mode_expiration
	actions.mode.enable("user.mouse")
	if mouse_mode_expiration is not None:
		cron.cancel(mouse_mode_expiration)
	mouse_mode_expiration = cron.after(duration, lambda: actions.mode.disable("user.mouse"))

@mod.action_class
class Actions:
	def gamepad_disable_autorelease():
		"""Disable south button autorelease (for mouse dragging)"""
		global allow_autorelease, scheduled_actions
		allow_autorelease = False
	   	# Cancel any existing scheduled autoreleases
		for button, job in scheduled_actions.items():
			cron.cancel(job)
		scheduled_actions.clear()

	def gamepad_enable_autorelease():
		"""Re-enable south button autorelease"""
		global allow_autorelease, scheduled_actions
		allow_autorelease = True

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

	def gamepad_press_left_trigger():
		"""Gamepad press button left trigger"""
		global trigger_jobs
		trigger_jobs["left"] = cron.interval("128ms", lambda: gamepad_scroll(0, -1.15))

	def gamepad_release_left_trigger(held: int):
		"""Gamepad release button left trigger"""
		cron.cancel(trigger_jobs["left"])

	def gamepad_press_right_trigger():
		"""Gamepad press button right trigger"""
		global trigger_jobs
		trigger_jobs["right"] = cron.interval("128ms", lambda: gamepad_scroll(0, 1.15))

	def gamepad_release_right_trigger(held: int):
		"""Gamepad release button right trigger"""
		cron.cancel(trigger_jobs["right"])
		
	# Stick buttons

	def gamepad_press_left_stick():
		"""Gamepad press button left thumb stick"""
		global need_to_go_back_to_sleep, stick_holding
		# Check if the right stick is already being held (we're in long mode from right stick)
		if stick_holding == "right":
			# We're already in long mode from the other stick, do focus last
			actions.mimic("focus last")
		else:
			# Normal long mode activation
			stick_holding = "left"
			if not actions.speech.enabled():
				actions.speech.enable()
				need_to_go_back_to_sleep = True
			actions.mimic("long mode")
	
	def gamepad_release_left_stick(held: int):
		"""Gamepad release button left thumb stick"""
		global need_to_go_back_to_sleep, stick_holding
		# Only exit long mode if this was the stick that initiated it
		if stick_holding == "left":
			stick_holding = None
			actions.mimic("done with long mode")
			if need_to_go_back_to_sleep:
				actions.speech.disable()
				need_to_go_back_to_sleep = False
	
	def gamepad_press_right_stick():
		"""Gamepad press button right thumb stick"""
		global need_to_go_back_to_sleep, stick_holding
		# Check if the left stick is already being held (we're in long mode from left stick)
		if stick_holding == "left":
			# We're already in long mode from the other stick, do focus last
			actions.mimic("focus last")
		else:
			# Normal long mode activation
			stick_holding = "right"
			if not actions.speech.enabled():
				actions.speech.enable()
				need_to_go_back_to_sleep = True
			actions.mimic("long mode")
	
	def gamepad_release_right_stick(held: int):
		"""Gamepad release button right thumb stick"""
		global need_to_go_back_to_sleep, stick_holding
		# Only exit long mode if this was the stick that initiated it
		if stick_holding == "right":
			stick_holding = None
			actions.mimic("done with long mode")
			if need_to_go_back_to_sleep:
				actions.speech.disable()
				need_to_go_back_to_sleep = False

	# Analog thumb sticks

	def gamepad_stick_left(x: float, y: float):
		"""Gamepad left stick movement"""
		initiate_mouse_mode("1s")
		gamepad_mouse_move(x, y, 0.05)

	def gamepad_stick_right(x: float, y: float):
		"""Gamepad right stick movement"""
		initiate_mouse_mode()
		gamepad_mouse_move(x, y, 0.3)

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
			case "left_trigger":
				actions.user.gamepad_release_left_trigger(held)
			case "right_trigger":
				actions.user.gamepad_release_right_trigger(held)
			case "left_stick":
				actions.user.gamepad_release_left_stick(held)
			case "right_stick":
				actions.user.gamepad_release_right_stick(held)
			case _:
				raise ValueError(f"Unknown button: {button}")

	def gamepad_button_down(button: str):
		"""Gamepad press button <button>"""
		timestamps[button] = time.perf_counter()
		if allow_autorelease and button in buttons_with_autorelease:
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
			case "left_trigger":
				actions.user.gamepad_press_left_trigger()
			case "right_trigger":
				actions.user.gamepad_press_right_trigger()
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
		if button in buttons_with_autorelease and button in scheduled_actions:
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



def gamepad_mouse_move(dx: float, dy: float, multiplier: float):
	"""Perform gamepad mouse cursor movement"""
	x, y = ctrl.mouse_pos()
	screen = get_screen(x, y)
	# Check if we're near max deflection
	magnitude = max(abs(dx), abs(dy))
	if magnitude > 0.98:
		# Boost speed significantly at near-max deflection
		dx = dx**3 * screen.dpi * multiplier * 3.0
		dy = dy**3 * screen.dpi * multiplier * 3.0
	else:
		# Normal cubic scaling for precise movement
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

