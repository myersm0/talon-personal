from talon import Context

from . import bindings

context = Context()
context.matches = """
mode: user.long
and not mode: user.meeting
"""

bindings.install(context, {
	"dpad_left":     bindings.mimic_phrase("focus last"),
	"dpad_right":    bindings.mimic_phrase("focus last"),
	"dpad_up":       bindings.mimic_phrase("window next"),
	"dpad_down":     bindings.mimic_phrase("window last"),
	"north":         bindings.mimic_phrase("window next"),
	"south":         bindings.mimic_phrase("window last"),
	"west":          bindings.mimic_phrase("focus last"),
	"east":          bindings.mimic_phrase("focus last"),
	"select":        bindings.mimic_phrase("set dummy Mike"),
	"start":         bindings.mimic_phrase("set default Mike"),
	"left_trigger":  bindings.mimic_phrase("undo"),
	"right_trigger": bindings.mimic_phrase("redo"),
})
