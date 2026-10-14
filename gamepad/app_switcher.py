from talon import app, imgui, ui

recent_app_names = []
choices = []
selected_index = 0
offsets = {"previous": -1, "next": 1}


def remember(application):
	if application.name in recent_app_names:
		recent_app_names.remove(application.name)
	recent_app_names.insert(0, application.name)


def recency(application) -> int:
	if application.name in recent_app_names:
		return recent_app_names.index(application.name)
	return len(recent_app_names)


@imgui.open()
def picker(gui: imgui.GUI):
	for index, application in enumerate(choices):
		marker = "▶" if index == selected_index else "  "
		gui.text(f"{marker} {application.name}")


def open_picker():
	global choices, selected_index
	remember(ui.active_app())
	choices = sorted(ui.apps(background=False), key=recency)
	selected_index = min(1, len(choices) - 1)
	picker.show()


def step(direction: str):
	global selected_index
	selected_index = (selected_index + offsets[direction]) % len(choices)
	picker.show()


def close_picker():
	picker.hide()
	choices[selected_index].focus()


def on_ready():
	remember(ui.active_app())
	ui.register("app_activate", remember)


app.register("ready", on_ready)
