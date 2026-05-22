# modes/

Custom Talon modes for this setup. Modes are declared in `modes.py`, enabled/disabled from voice in `modes.talon`, and have their per-mode behavior in the remaining files.

The full set: `user.long`, `user.recording`, `user.meeting`, `user.seek`, `user.mouse`, `user.symbol`.

## Files

### `modes.py`
Declares all six custom modes. Just `mod.mode(name, desc=...)` calls.

### `modes.talon`
Voice commands to enter and exit modes. Every command is regex-anchored (`^...$`) so it only fires as a standalone utterance. Mode-entering commands are short (`meeting mode`, `long mode`, `symbol mode`); exits use the `done with X` pattern.

Note that `^done with seeking$` keys `q` rather than calling `mode.disable("user.seek")` directly — the actual disable is handled by `seek.talon`'s `key(q)` handler, which keeps the keypress and mode toggle in one place.

### `long.talon`
While `user.long` is active, sets `speech.timeout` to 0.7s. This overrides both the command-mode default of 0.25s and the dictation-mode default of 1.0s (both set in `overrides/`, both gated by `not mode: user.long`). Use case: speaking something tricky to pronounce or a long mouthful you don't want the engine to cut off mid-utterance.

### `meeting.talon`
Push-to-talk for Zoom and other calls. While in meeting mode:

- F5 hold enables speech; F5 release disables it.
- Gamepad L3 (left stick click) hold/release mirrors F5.
- `^command mode$` / `^end of meeting$` exits meeting mode, restores the default mic, and re-enables speech.

This is an inverted-polarity setup vs. normal operation. In normal mode (per `core/general.talon`), speech is on by default and F6 is push-to-mute. In meeting mode, speech is off by default and F5 is push-to-talk. The polarity flip is what makes meeting mode safe on calls — stray utterances are ignored, but a single physical key (or gamepad button) lets a real command through.

### `recording.talon`
The `take note` and `take context` commands shell out to external scripts in `$HOME/bin/` (`take_note`, `take_context`) via `core/general.py`'s `run_external_command`. Each command also disables speech and enables `user.recording` mode.

The context header is `not mode: recording`, so these commands can only fire from outside recording mode — there's no risk of accidentally re-triggering while the popup is still open. The mode itself has no commands defined; by design, recording mode is when Talon stays out of the way.

### `seek.talon`
Active when in `user.seek` and not in recording. Two keys are intercepted to exit the mode cleanly:

- `enter` disables seek mode then forwards the enter keypress.
- `q` disables seek mode then forwards the q keypress.

The intended workflow is tmux seeking (copy mode); enter selects, q quits, and either way Talon's mode tracking stays in sync with what tmux is actually doing.

## Mode interaction notes

The `user.long` mode interacts with the timeout settings in `overrides/settings_command.talon` and `overrides/settings_dictation.talon`, both of which are gated by `not mode: user.long`. When entering long mode, those settings deactivate and `long.talon`'s 0.7s timeout takes over for both command and dictation. Future-you should update both sides if changing timeout policies.

`user.meeting` and `user.recording` both disable Talon speech on entry but for different reasons: meeting mode protects against stray utterances during a call (with F5/L3 as the escape hatch); recording mode protects against Talon trying to interpret what you're typing into a note-taking popup (no escape hatch needed because the popup closes the mode).

`user.symbol` is declared for entering special characters via gamepad — the actual gamepad-to-symbol bindings live in `gamepad/`.

`user.mouse` is deliberately entered only from the gamepad and has no voice command for entry. Any thumbstick movement triggers it with a 3-second decay; while active, the normal gamepad button bindings are overridden to enable mouse-click behavior. The disable command (`^done with mouse$` in `modes.talon`) exists as a manual override but in normal use the timeout handles it. See `gamepad/` for the implementation.
