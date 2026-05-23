from talon import actions


def skip_press():
	actions.skip()


def skip_release(held):
	actions.skip()


def repeat_key(key):
	return (
		lambda: actions.user.key_hold(key),
		lambda held: actions.user.key_release(key),
	)


def tap_key(key):
	return (skip_press, lambda held: actions.key(key))


def press_key(key):
	return (lambda: actions.key(key), skip_release)


def tap_keys(*keys):
	def release(held):
		for key in keys:
			actions.key(key)
	return (skip_press, release)


def tap_call(action):
	return (skip_press, lambda held: action())


def by_hold(*specifications):
	def to_function(specification):
		if isinstance(specification, str):
			return lambda key=specification: actions.key(key)
		return specification
	functions = [to_function(specification) for specification in specifications]
	def release(held):
		functions[min(held, len(functions) - 1)]()
	return (skip_press, release)


def mimic_phrase(phrase):
	return (skip_press, lambda held: actions.mimic(phrase))


def hold(press_action, release_action):
	return (press_action, lambda held: release_action())


def install(context, bindings_by_button):
	methods = {}
	for button, (press_function, release_function) in bindings_by_button.items():
		methods[f"gamepad_press_{button}"] = press_function
		methods[f"gamepad_release_{button}"] = release_function
	context.action_class("user")(type("GamepadBindings", (), methods))
