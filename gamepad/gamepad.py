from talon import Module, Context, actions, ui, ctrl
from talon.screen import Screen
import time

HOLD_TIMEOUT1 = 0.3
HOLD_TIMEOUT2 = 0.8

screen: Screen = ui.main_screen()
mod = Module()
slow_scroll = False
slow_mouse_move = False
timestamps = {}


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
        actions.user.command_dictation_mode_toggle()

    def gamepad_release_start(held: int):
        """Gamepad release button start"""
        if held:
            actions.user.command_dictation_mode_toggle()

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
        gamepad_scroll_slow_toggle()

    def gamepad_release_left_stick(held: int):
        """Gamepad release button left thumb stick"""
        actions.skip()

    def gamepad_press_right_stick():
        """Gamepad press button right thumb stick"""
        gamepad_mouse_move_slow_toggle()

    def gamepad_release_right_stick(held: int):
        """Gamepad release button right thumb stick"""
        actions.skip()

    # Analog triggers

    def gamepad_trigger_left(value: float):
        """Gamepad trigger left movement"""
        gamepad_scroll(0, value * -1)

    def gamepad_trigger_right(value: float):
        """Gamepad trigger right movement"""
        gamepad_scroll(0, value)

    # Analog thumb sticks

    def gamepad_stick_left(x: float, y: float):
        """Gamepad left stick movement"""
        gamepad_scroll(x, y)

    def gamepad_stick_right(x: float, y: float):
        """Gamepad right stick movement"""
        gamepad_mouse_move(x, y)

    # Scaffolding actions used by the Talon file

    def gamepad_button_down(button: str):
        """Gamepad press button <button>"""
        timestamps[button] = time.perf_counter()

        match button:
            # DPAD buttons
            case "dpad_left":
                actions.user.gamepad_press_dpad_left()
            case "dpad_up":
                actions.user.gamepad_press_dpad_up()
            case "dpad_right":
                actions.user.gamepad_press_dpad_right()
            case "dpad_down":
                actions.user.gamepad_press_dpad_down()

            # Compass / ABXY buttons
            case "west":
                actions.user.gamepad_press_west()
            case "north":
                actions.user.gamepad_press_north()
            case "east":
                actions.user.gamepad_press_east()
            case "south":
                actions.user.gamepad_press_south()

            # Select / Start buttons
            case "select":
                actions.user.gamepad_press_select()
            case "start":
                actions.user.gamepad_press_start()

            # Shoulder buttons
            case "left_shoulder":
                actions.user.gamepad_press_left_shoulder()
            case "right_shoulder":
                actions.user.gamepad_press_right_shoulder()

            # Stick buttons
            case "left_stick":
                actions.user.gamepad_press_left_stick()
            case "right_stick":
                actions.user.gamepad_press_right_stick()

            case _:
                raise ValueError(f"Unknown button: {button}")

    def gamepad_button_up(button: str):
        """Gamepad release button <button>"""
        duration = time.perf_counter() - timestamps[button]
        if duration > HOLD_TIMEOUT2:
            held = 2
        elif duration > HOLD_TIMEOUT1:
            held = 1
        else:
            held = 0

        match button:
            # DPAD buttons
            case "dpad_left":
                actions.user.gamepad_release_dpad_left(held)
            case "dpad_up":
                actions.user.gamepad_release_dpad_up(held)
            case "dpad_right":
                actions.user.gamepad_release_dpad_right(held)
            case "dpad_down":
                actions.user.gamepad_release_dpad_down(held)

            # Compass / ABXY buttons
            case "west":
                actions.user.gamepad_release_west(held)
            case "north":
                actions.user.gamepad_release_north(held)
            case "east":
                actions.user.gamepad_release_east(held)
            case "south":
                actions.user.gamepad_release_south(held)

            # Select / Start buttons
            case "select":
                actions.user.gamepad_release_select(held)
            case "start":
                actions.user.gamepad_release_start(held)

            # Shoulder buttons
            case "left_shoulder":
                actions.user.gamepad_release_left_shoulder(held)
            case "right_shoulder":
                actions.user.gamepad_release_right_shoulder(held)

            # Stick buttons
            case "left_stick":
                actions.user.gamepad_release_left_stick(held)
            case "right_stick":
                actions.user.gamepad_release_right_stick(held)

            case _:
                raise ValueError(f"Unknown button: {button}")


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

    # # Move one fourth of screen width/height
    # match direction:
    #     case "up":
    #         y -= rect.height / 4
    #     case "down":
    #         y += rect.height / 4
    #     case "left":
    #         x -= rect.width / 4
    #     case "right":
    #         x += rect.width / 4

    actions.mouse_move(x, y)


def get_screen(x: float, y: float) -> Screen:
    global screen
    if not screen.contains(x, y):
        screen = ui.screen_containing(x, y)
    return screen






ctx_general = Context()
ctx_general.matches = """
not app: /terminal/i
and not app: /term/i
and not app: /julia/i
and not app: /zoom/i
and not app: /safari/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
"""

@ctx_general.action_class("user")
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
        actions.user.key_hold("space")
    def gamepad_release_north(held):
        actions.user.key_release("space")

    def gamepad_press_south():
        actions.user.key_hold("enter")
    def gamepad_release_south(held):
        actions.user.key_release("enter")

    def gamepad_press_west():
        actions.user.key_hold("backspace")
    def gamepad_release_west(held):
        actions.user.key_release("backspace")

    def gamepad_press_east():
        actions.user.key_hold(".")
    def gamepad_release_east(held):
        actions.user.key_release(".")

    def gamepad_press_left_shoulder():
        actions.key("ctrl-pageup")
    def gamepad_release_left_shoulder(held):
        actions.skip()

    def gamepad_press_right_shoulder():
        actions.key("ctrl-pagedown")
    def gamepad_release_right_shoulder(held):
        actions.skip()

    def gamepad_press_left_stick():
        actions.key("shift:down")
    def gamepad_release_left_stick(held):
        actions.key("shift:up")

    def gamepad_press_right_stick():
        actions.key("cmd:down")
    def gamepad_release_right_stick(held):
        actions.key("cmd:up")

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        if held == 0:
            actions.key("cmd-w")
        else:
            actions.key("cmd-q")

    def gamepad_press_start():
        actions.skip()
    def gamepad_release_start(held):
        if held == 0:
            actions.key("cmd-t")
        elif held == 1:
            actions.key("cmd-n")
        elif held == 2:
            actions.key("cmd-shift-n")



ctx_terminal = Context()
ctx_terminal.matches = """
app: /terminal/i
app: /term/i
not mode: user.seek
and not mode: user.symbol
and not mode: user.recording
"""

@ctx_terminal.action_class("user")
class GeneralActions:
    def gamepad_press_dpad_left():
        actions.key("escape")
        actions.user.key_hold("b")
    def gamepad_release_dpad_left(held):
        actions.user.key_release("b")

    def gamepad_press_dpad_right():
        actions.key("escape")
        actions.user.key_hold("w")
    def gamepad_release_dpad_right(held):
        actions.user.key_release("w")

    def gamepad_press_dpad_up():
        actions.key("escape")
        actions.user.key_hold("k")
    def gamepad_release_dpad_up(held):
        actions.user.key_release("k")

    def gamepad_press_dpad_down():
        actions.key("escape")
        actions.user.key_hold("j")
    def gamepad_release_dpad_down(held):
        actions.user.key_release("j")

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
        if held == 0:
            actions.key("enter")
        elif held >= 1:
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

    def gamepad_press_left_shoulder():
        actions.skip()
    def gamepad_release_left_shoulder(held):
        if held == 0:
            actions.key("escape")
            actions.key("f12")
        elif held == 1:
            actions.key("escape")
            actions.key("0")
        elif held == 2:
            actions.key("escape")
            actions.insert("gg")

    def gamepad_press_right_shoulder():
        actions.skip()
    def gamepad_release_right_shoulder(held):
        if held == 0:
            actions.key("tab")
        elif held == 1:
            actions.key("escape")
            actions.key("shift-A")
        elif held == 2:
            actions.key("escape")
            actions.key("G")

    def gamepad_trigger_left(value: float):
        """Gamepad trigger left movement"""
        if value > 0.8:
            actions.key("escape")
            actions.key("u")

    def gamepad_trigger_right(value: float):
        """Gamepad trigger right movement"""
        if value > 0.8:
            actions.key("escape")
            actions.key("ctrl-r")

    def gamepad_press_left_stick():
        actions.skip()
    def gamepad_release_left_stick(held):
        actions.key("/")

    def gamepad_press_right_stick():
        actions.skip()
    def gamepad_release_right_stick(held):
        actions.key('"')

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        if held >= 1:
            actions.insert("exit")
            actions.key("enter")

    def gamepad_press_start():
        actions.skip()
    def gamepad_release_start(held):
        if held == 0:
            actions.key("cmd-t")
        elif held >= 1:
            actions.key("cmd-n")


ctx_julia = Context()
ctx_julia.matches = """
app: /julia/i
"""

@ctx_julia.action_class("user")
class JuliaActions:
    def gamepad_press_dpad_left():
        actions.user.key_hold("left", "32ms")
    def gamepad_release_dpad_left(held):
        actions.user.key_release("left")

    def gamepad_press_dpad_right():
        actions.user.key_hold("right", "32ms")
    def gamepad_release_dpad_right(held):
        actions.user.key_release("right")

    def gamepad_press_dpad_up():
        actions.skip()
    def gamepad_release_dpad_up(held):
        actions.key("up")

    def gamepad_press_dpad_down():
        actions.skip()
    def gamepad_release_dpad_down(held):
        actions.key("down")

    def gamepad_press_north():
        actions.skip()
    def gamepad_release_north(held):
        actions.key("space")

    def gamepad_press_south():
        actions.skip()
    def gamepad_release_south(held):
        actions.key("enter")

    def gamepad_press_west():
        actions.skip()
    def gamepad_release_west(held):
        actions.key("backspace")

    def gamepad_press_east():
        actions.skip()
    def gamepad_release_east(held):
        actions.key("q")

    def gamepad_press_left_shoulder():
        actions.key("ctrl-pageup")
    def gamepad_release_left_shoulder(held):
        actions.skip()

    def gamepad_press_right_shoulder():
        actions.key("ctrl-pagedown")
    def gamepad_release_right_shoulder(held):
        actions.skip()

    def gamepad_trigger_left(value: float):
        """Gamepad trigger left movement"""
        if value > 0.8:
            actions.key(",")

    def gamepad_trigger_right(value: float):
        """Gamepad trigger right movement"""
        if value > 0.8:
            actions.key(".")

    def gamepad_press_left_stick():
        actions.skip()
    def gamepad_release_left_stick(held):
        actions.key("0")

    def gamepad_press_right_stick():
        actions.skip()
    def gamepad_release_right_stick(held):
        actions.key('$')

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        actions.key("e")

    def gamepad_press_start():
        actions.skip()
    def gamepad_release_start(held):
        actions.key("a")


ctx_meeting = Context()
ctx_meeting.matches = """
mode: user.meeting
"""

@ctx_meeting.action_class("user")
class MeetingActions:
    def gamepad_press_left_stick():
        actions.speech.enable()
    def gamepad_release_left_stick(held):
        actions.speech.disable()


ctx_zoom = Context()
ctx_zoom.matches = """
app: /zoom/i
"""

@ctx_zoom.action_class("user")
class ZoomActions:
    def gamepad_press_right_stick():
        actions.skip()
    def gamepad_release_right_stick(held):
        if held >= 1:
            actions.key("cmd-shift-a")

    def gamepad_press_select():
        actions.skip()
    def gamepad_release_select(held):
        if held >= 1:
            actions.key("cmd-q")


ctx_recording1 = Context()
ctx_recording1.matches = """
mode: user.recording
and not mode: user.meeting
"""

@ctx_recording1.action_class("user")
class Recording1Actions:
    def gamepad_press_east():
        actions.key("ctrl-c")
    def gamepad_release_east(held):
        actions.user.unmute()
        actions.mode.disable("user.recording")
        actions.speech.enable()
        print("Waking up.")


ctx_recording2 = Context()
ctx_recording2.matches = """
mode: user.recording
and mode: user.meeting
"""

@ctx_recording2.action_class("user")
class Recording2Actions:
    def gamepad_press_east():
        actions.key("ctrl-c")
    def gamepad_release_east(held):
        actions.user.unmute()
        actions.mode.disable("user.recording")
        print("Not waking up because we're in a meeting.")


ctx_safari = Context()
ctx_safari.matches = """
app: /safari/i
"""

@ctx_safari.action_class("user")
class SafariActions:
    def gamepad_press_dpad_left():
        actions.skip()
    def gamepad_release_dpad_left(held):
        actions.key("left")

    def gamepad_press_dpad_right():
        actions.skip()
    def gamepad_release_dpad_right(held):
        actions.key("right")

    def gamepad_press_dpad_up():
        actions.skip()
    def gamepad_release_dpad_up(held):
        actions.key("up")

    def gamepad_press_dpad_down():
        actions.skip()
    def gamepad_release_dpad_down(held):
        actions.key("down")

    def gamepad_press_north():
        actions.skip()
    def gamepad_release_north(held):
        actions.key("enter")

    def gamepad_press_south():
        actions.skip()
    def gamepad_release_south(held):
        actions.mouse_click(0)

    def gamepad_press_west():
        actions.skip()
    def gamepad_release_west(held):
        actions.key("escape")

    def gamepad_press_east():
        actions.skip()
    def gamepad_release_east(held):
        actions.key("escape")

