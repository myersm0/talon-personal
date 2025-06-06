from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

# workaround for the fact that the analogue sticks seem to generate 4 presses at a time
stick_move_counter = 0

ctx_terminal = Context()
ctx_terminal.matches = """
app: /terminal/i
app: /term/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
and not mode: user.long
"""

@ctx_terminal.action_class("user")
class GeneralActions:
	def gamepad_press_dpad_left():
		actions.user.key_hold("left")
	def gamepad_release_dpad_left(held):
		actions.user.key_release("left")

	def gamepad_press_dpad_right():
		actions.user.key_hold("right")
	def gamepad_release_dpad_right(held):
		actions.user.key_release("right")

	def gamepad_press_dpad_up():
		actions.user.key_hold("up")
	def gamepad_release_dpad_up(held):
		actions.user.key_release("up")

	def gamepad_press_dpad_down():
		actions.user.key_hold("down")
	def gamepad_release_dpad_down(held):
		actions.user.key_release("down")

	def gamepad_press_north():
		actions.skip()
	def gamepad_release_north(held):
		if held == 0:
			actions.key("space")
		elif held == 1:
			actions.insert("y$")
		elif held == 2:
			actions.insert("yy")

	def gamepad_press_south():
		actions.skip()
	def gamepad_release_south(held):
		if held < 2:
			actions.key("enter")
		else:
			actions.key("escape")
			actions.insert("p")

	def gamepad_press_west():
		actions.skip()
	def gamepad_release_west(held):
		if held == 0:
			actions.key("backspace")
		elif held == 1:
			actions.insert("d$")
		elif held == 2:
			actions.insert("dd")

	def gamepad_press_east():
		actions.skip()
	def gamepad_release_east(held):
		if held == 0:
			actions.key("ctrl-c")
		elif held == 1:
			actions.insert("c$")
		elif held == 2:
			actions.insert("cc")

	def gamepad_press_select():
		actions.skip()
	def gamepad_release_select(held):
		if held == 2:
			actions.insert("exit")
			actions.key("enter")

	def gamepad_press_start():
		actions.skip()
	def gamepad_release_start(held):
		if held < 2:
			actions.key("cmd-t")
		else:
			actions.key("cmd-n")

	def gamepad_press_left_shoulder():
		actions.skip()
	def gamepad_release_left_shoulder(held):
		actions.key("escape")
		actions.key("f12")

	def gamepad_press_right_shoulder():
		actions.skip()
	def gamepad_release_right_shoulder(held):
		if held < 2:
			actions.key("tab")
		else:
			actions.key("escape")
			actions.key("shift-A")

	def gamepad_press_left_trigger():
		actions.skip()

	def gamepad_release_left_trigger(held):
		actions.key("escape")
		actions.key("g")
		actions.key("g")

	def gamepad_press_right_trigger():
		actions.skip()

	def gamepad_release_right_trigger(held):
		actions.key("escape")
		actions.key("G")

	def gamepad_stick_right(x: float, y: float):
		"""Gamepad right stick movement"""
		global stick_move_counter
		ratio = x / y
		axis = "x" if abs(ratio) > 1 else "y"
		positive_direction = x > 0 if axis == "x" else y > 0
		if axis == "x" and positive_direction:
			move = "right"
		elif axis == "x":
			move = "left"
		elif axis == "y" and positive_direction:
			move = "down"
		elif axis == "y":
			move = "up"
		magnitude = max(abs(x), abs(y))
		movement_threshold = 8 if magnitude < 0.9 else 1
		if magnitude >= 0.9:
			move = f"{move}:8"
		stick_move_counter += 1
		if stick_move_counter >= movement_threshold:
			actions.key(move)
			stick_move_counter = 0

	def gamepad_stick_left(x: float, y: float):
		"""Gamepad right stick movement"""
		global stick_move_counter
		ratio = x / y
		axis = "x" if abs(ratio) > 1 else "y"
		positive_direction = x > 0 if axis == "x" else y > 0
		if axis == "x" and positive_direction:
			move = "w"
		elif axis == "x":
			move = "b"
		elif axis == "y" and positive_direction:
			move = "j"
		elif axis == "y":
			move = "k"
		magnitude = max(abs(x), abs(y))
		movement_threshold = 8 if magnitude < 0.9 else 1
		if magnitude >= 0.9:
			move = f"{move}:8"
		stick_move_counter += 1
		if stick_move_counter >= movement_threshold:
			actions.key("escape")
			actions.key(move)
			stick_move_counter = 0
