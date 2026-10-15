from talon import Module, actions, ui, ctrl, cron
import time

from . import picker

hold_timeout_short = 0.3
hold_timeout_long = 0.8

mod = Module()
timestamps = {}
scheduled_actions = {}
buttons_held = set()

buttons = (
	"dpad_left", "dpad_up", "dpad_right", "dpad_down",
	"west", "north", "east", "south",
	"select", "start",
	"left_shoulder", "right_shoulder",
	"left_paddle", "right_paddle",
	"left_function", "right_function",
)

buttons_with_autorelease = (
	"north", "south", "west", "east",
	"start", "select",
	"left_shoulder", "right_shoulder",
)

picker_directions = {
	"dpad_left": "previous",
	"dpad_up": "previous",
	"left_shoulder": "previous",
	"dpad_right": "next",
	"dpad_down": "next",
	"right_shoulder": "next",
}

buttons_pressed_in_picker = set()
allow_autorelease = True


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
		"""Gamepad press button select (Create on the DualSense)"""
		actions.user.quick_pick_show()

	def gamepad_release_select(held: int):
		"""Gamepad release button select (Create on the DualSense)"""
		actions.skip()

	def gamepad_press_start():
		"""Gamepad press button start (Options on the DualSense)"""
		actions.skip()

	def gamepad_release_start(held: int):
		"""Gamepad release button start (Options on the DualSense)"""
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

	def gamepad_press_left_paddle():
		"""Gamepad press left back paddle"""
		picker.open_window_picker()

	def gamepad_release_left_paddle(held: int):
		"""Gamepad release left back paddle"""
		picker.close_picker()

	def gamepad_press_right_paddle():
		"""Gamepad press right back paddle"""
		picker.open_app_picker()

	def gamepad_release_right_paddle(held: int):
		"""Gamepad release right back paddle"""
		picker.close_picker()

	def gamepad_press_left_function():
		"""Gamepad press left Fn button"""
		actions.user.take_screenshot()

	def gamepad_release_left_function(held: int):
		"""Gamepad release left Fn button"""
		actions.skip()

	def gamepad_press_right_function():
		"""Gamepad press right Fn button"""
		actions.user.save_selected_text_to_file()

	def gamepad_release_right_function(held: int):
		"""Gamepad release right Fn button"""
		actions.skip()

	def gamepad_action_dispatch(button: str, held: int):
		"""Dispatch a release for the given button"""
		if button not in buttons:
			raise ValueError(f"Unknown button: {button}")
		getattr(actions.user, f"gamepad_release_{button}")(held)

	def gamepad_button_down(button: str):
		"""Gamepad press button <button>"""
		if button not in buttons:
			raise ValueError(f"Unknown button: {button}")
		if button in buttons_held or button in buttons_pressed_in_picker:
			return
		if picker.picker.showing and button in picker_directions:
			buttons_pressed_in_picker.add(button)
			picker.step(picker_directions[button])
			return
		buttons_held.add(button)
		timestamps[button] = time.perf_counter()
		if allow_autorelease and button in buttons_with_autorelease:
			scheduled_actions[button] = cron.after(
				"800ms",
				lambda: actions.user.gamepad_action_dispatch(button, 2),
			)
		getattr(actions.user, f"gamepad_press_{button}")()

	def gamepad_button_up(button: str):
		"""Gamepad release button <button>"""
		if button in buttons_pressed_in_picker:
			buttons_pressed_in_picker.remove(button)
			return
		if button not in buttons_held:
			return
		buttons_held.remove(button)
		duration = time.perf_counter() - timestamps[button]
		if duration > hold_timeout_long:
			held = 2
		elif duration > hold_timeout_short:
			held = 1
		else:
			held = 0
		if button in scheduled_actions:
			job = scheduled_actions.pop(button)
			cron.cancel(job)
			if cron.time.perf_counter() >= job.expiry:
				return
		actions.user.gamepad_action_dispatch(button, held)


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
