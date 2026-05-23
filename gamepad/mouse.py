from talon import Context, actions

from . import bindings

context = Context()
context.matches = """
mode: user.mouse
"""


def south_press():
	actions.user.gamepad_disable_autorelease()
	actions.mouse_drag(0)


def south_release():
	actions.mouse_release(0)
	actions.user.gamepad_enable_autorelease()


def north_press():
	actions.key("cmd:down")


def north_release():
	actions.mouse_click(0)
	actions.key("cmd:up")


def west_press():
	actions.key("shift:down")


def west_release():
	actions.mouse_click(0)
	actions.key("shift:up")


bindings.install(context, {
	"south": bindings.hold(south_press, south_release),
	"east":  bindings.tap_call(lambda: actions.mouse_click(1)),
	"north": bindings.hold(north_press, north_release),
	"west":  bindings.hold(west_press, west_release),
})
