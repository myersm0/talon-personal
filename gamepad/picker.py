from talon import app, imgui, ui

recent_app_names = []
choices = []
labels = []
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


def is_choosable(window) -> bool:
	return not window.hidden and len(window.title) > 0


@imgui.open()
def picker(gui: imgui.GUI):
	for index, label in enumerate(labels):
		marker = "▶" if index == selected_index else "  "
		gui.text(f"{marker} {label}")


def open_picker(new_choices: list, label_of):
	global choices, labels, selected_index
	choices = new_choices
	labels = [label_of(choice) for choice in choices]
	selected_index = min(1, len(choices) - 1)
	if choices:
		picker.show()


def open_app_picker():
	remember(ui.active_app())
	open_picker(
		sorted(ui.apps(background=False), key=recency),
		lambda application: application.name,
	)


def open_window_picker():
	open_picker(
		[window for window in ui.active_app().windows() if is_choosable(window)],
		lambda window: window.title,
	)


def step(direction: str):
	global selected_index
	selected_index = (selected_index + offsets[direction]) % len(choices)
	picker.show()


def close_picker():
	if not choices:
		return
	picker.hide()
	choices[selected_index].focus()


def on_ready():
	remember(ui.active_app())
	ui.register("app_activate", remember)


app.register("ready", on_ready)
