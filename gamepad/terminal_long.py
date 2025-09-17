from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

# workaround for the fact that the analogue sticks seem to generate 4 presses at a time
stick_move_counter = 0

ctx_terminal = Context()
ctx_terminal.matches = """
app: /terminal/i
app: /term/i
mode: user.long
and not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
and not mode: user.mouse
"""

@ctx_terminal.action_class("user")
class GeneralActions:
	def gamepad_press_dpad_left():
		actions.skip()
	def gamepad_release_dpad_left(held):
		actions.key("ctrl-a")
		actions.key("h")

	def gamepad_press_dpad_right():
		actions.skip()
	def gamepad_release_dpad_right(held):
		actions.key("ctrl-a")
		actions.key("l")

	def gamepad_press_dpad_up():
		actions.skip()
	def gamepad_release_dpad_up(held):
		actions.key("ctrl-a")
		actions.key("k")

	def gamepad_press_dpad_down():
		actions.skip()
	def gamepad_release_dpad_down(held):
		actions.key("ctrl-a")
		actions.key("j")

	def gamepad_press_left_shoulder():
		actions.skip()
	def gamepad_release_left_shoulder(held):
		actions.key("escape")
		actions.key("u")

	def gamepad_press_right_shoulder():
		actions.skip()
	def gamepad_release_right_shoulder(held):
		actions.key("escape")
		actions.key("ctrl-r")

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
			stick_move_counter = 1

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
		movement_threshold = 4 if magnitude < 0.9 else 1
		if magnitude >= 0.9:
			move = f"{move}:8"
		stick_move_counter += 1
		if stick_move_counter >= movement_threshold:
			actions.key("escape")
			actions.key(move)
			stick_move_counter = 1
