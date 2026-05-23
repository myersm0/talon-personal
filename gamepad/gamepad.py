from talon import Module, actions, ui, ctrl, cron
from talon.screen import Screen
import time

hold_timeout_short = 0.3
hold_timeout_long = 0.8

screen: Screen = ui.main_screen()
mod = Module()
slow_scroll = False
timestamps = {}
scheduled_actions = {}
trigger_jobs = {}

buttons = (
	"dpad_left", "dpad_up", "dpad_right", "dpad_down",
	"west", "north", "east", "south",
	"select", "start",
	"left_shoulder", "right_shoulder",
	"left_trigger", "right_trigger",
	"left_stick", "right_stick",
)

buttons_with_autorelease = (
	"north", "south", "west", "east",
	"start", "select",
	"left_shoulder", "right_shoulder",
)

need_to_go_back_to_sleep = False
stick_holding = None
allow_autorelease = True
mouse_mode_expiration = None


def initiate_mouse_mode(duration: str = "3s"):
	global mouse_mode_expiration
	actions.mode.enable("user.mouse")
	if mouse_mode_expiration is not None:
		cron.cancel(mouse_mode_expiration)
	mouse_mode_expiration = cron.after(duration, lambda: actions.mode.disable("user.mouse"))


def long_mode_stick_press(side: str):
	global need_to_go_back_to_sleep, stick_holding
	other_side = "right" if side == "left" else "left"
	if stick_holding == other_side:
		actions.mimic("focus last")
		return
	stick_holding = side
	if not actions.speech.enabled():
		actions.speech.enable()
		need_to_go_back_to_sleep = True
	actions.mimic("long mode")


def long_mode_stick_release(side: str):
	global need_to_go_back_to_sleep, stick_holding
	if stick_holding != side:
		return
	stick_holding = None
	actions.mimic("done with long mode")
	if need_to_go_back_to_sleep:
		actions.speech.disable()
		need_to_go_back_to_sleep = False


@mod.action_class
class Actions:
	def gamepad_disable_autorelease():
		"""Disable south button autorelease (for mouse dragging)"""
		global allow_autorelease
		allow_autorelease = False
		for button, job in scheduled_actions.items():
			cron.cancel(job)
		scheduled_actions.clear()

	def gamepad_enable_autorelease():
		"""Re-enable south button autorelease"""
		global allow_autorelease
		allow_autorelease = True

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
		trigger_jobs["left"] = cron.interval("128ms", lambda: gamepad_scroll(0, -1.15))

	def gamepad_release_left_trigger(held: int):
		"""Gamepad release button left trigger"""
		cron.cancel(trigger_jobs["left"])

	def gamepad_press_right_trigger():
		"""Gamepad press button right trigger"""
		trigger_jobs["right"] = cron.interval("128ms", lambda: gamepad_scroll(0, 1.15))

	def gamepad_release_right_trigger(held: int):
		"""Gamepad release button right trigger"""
		cron.cancel(trigger_jobs["right"])

	def gamepad_press_left_stick():
		"""Gamepad press button left thumb stick"""
		long_mode_stick_press("left")

	def gamepad_release_left_stick(held: int):
		"""Gamepad release button left thumb stick"""
		long_mode_stick_release("left")

	def gamepad_press_right_stick():
		"""Gamepad press button right thumb stick"""
		long_mode_stick_press("right")

	def gamepad_release_right_stick(held: int):
		"""Gamepad release button right thumb stick"""
		long_mode_stick_release("right")

	def gamepad_stick_left(x: float, y: float):
		"""Gamepad left stick movement"""
		initiate_mouse_mode("1s")
		gamepad_mouse_move(x, y, 0.05)

	def gamepad_stick_right(x: float, y: float):
		"""Gamepad right stick movement"""
		initiate_mouse_mode()
		gamepad_mouse_move(x, y, 0.3)

	def gamepad_action_dispatch(button: str, held: int):
		"""Dispatch a release for the given button"""
		if button not in buttons:
			raise ValueError(f"Unknown button: {button}")
		getattr(actions.user, f"gamepad_release_{button}")(held)

	def gamepad_button_down(button: str):
		"""Gamepad press button <button>"""
		if button not in buttons:
			raise ValueError(f"Unknown button: {button}")
		timestamps[button] = time.perf_counter()
		if allow_autorelease and button in buttons_with_autorelease:
			scheduled_actions[button] = cron.after(
				"800ms",
				lambda: actions.user.gamepad_action_dispatch(button, 2),
			)
		getattr(actions.user, f"gamepad_press_{button}")()

	def gamepad_button_up(button: str):
		"""Gamepad release button <button>"""
		duration = time.perf_counter() - timestamps[button]
		if duration > hold_timeout_long:
			held = 2
		elif duration > hold_timeout_short:
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
	multiplier = 1.5 if slow_scroll else 3
	x = x**3 * multiplier
	y = y**3 * multiplier
	if x != 0 or y != 0:
		actions.mouse_scroll(x=x, y=y, by_lines=True)


def gamepad_mouse_move(delta_x: float, delta_y: float, multiplier: float):
	x, y = ctrl.mouse_pos()
	screen = get_screen(x, y)
	magnitude = (delta_x**2 + delta_y**2) ** 0.5
	if magnitude > 0.1:
		scaled_magnitude = magnitude**3
		delta_x = (delta_x / magnitude) * scaled_magnitude * screen.dpi * multiplier
		delta_y = (delta_y / magnitude) * scaled_magnitude * screen.dpi * multiplier
	else:
		delta_x = delta_x**3 * screen.dpi * multiplier
		delta_y = delta_y**3 * screen.dpi * multiplier
	actions.mouse_move(x + delta_x, y + delta_y)


def gamepad_scroll_slow_toggle():
	global slow_scroll
	slow_scroll = not slow_scroll


def gamepad_mouse_jump(direction: str):
	x, y = ctrl.mouse_pos()
	rect = ui.screen_containing(x, y).rect
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
