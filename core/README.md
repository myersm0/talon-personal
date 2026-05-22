# core/

Personal commands and utility modules that aren't specific to any one app or mode. The Python files expose actions consumed by the `.talon` files in this directory and elsewhere in `talon-personal/`.

## Files

### `general.talon`
A grab-bag of general commands: modifier hold/release, mode toggles (meeting, symbol, long, mouse — all declared in `modes/`), function-key bindings for speech and eye tracking control, window/workspace navigation, the screenshot and clip-this commands, surround/double helpers for symbols and letters, and assorted one-offs.

Two patterns worth noting:

- **Regex-anchored utterances** (`^stop$`, `^crunch$`, `^meeting mode$`, etc.) for commands that should only fire when spoken in isolation, not as part of a longer phrase.
- **Disambiguation aliases** for words the engine routinely mishears. 

### `general.py`
Action implementations called from `general.talon` and elsewhere:

- `concatenate(strings)` — utility join.
- `optional_enter(cmd)` — if `cmd == "go"` presses enter, otherwise presses space. Used to defer pressing enter on terminal commands; pairs with the `dont_go` list in `lists/` for the "go" / "but wait" / "then wait" terminal-command suffix pattern.
- `take_screenshot` — shells out to `$HOME/bin/screenshot` (external script; required prerequisite on any new machine).
- `set_default_mic` / `set_builtin_mic` — shells out to `$HOME/bin/select_mic` with a fallback list of USB mic names (Shure MVX2U, Samson Q9U, Wireless PRO RX, MacBook Pro Microphone).
- `run_external_command(program)` — opens a small Terminal.app window via AppleScript, runs the named program, exits. Currently used by `modes/recording.talon` for `take_note` and `take_context`.

### `clip.py`
`save_selected_text_to_file()` writes the current selection (or clipboard, as fallback) to a timestamped `.txt` file under `$CLIPS_DIR`, prefixed with a source line containing the active window's title. Called by `selection clip` / `clip this` in `general.talon`. `$CLIPS_DIR` is set in `environment/environment.py`.

### `hiss.py`
Adaptive hiss-as-left-click handler. Hiss is the primary click mechanism in this setup; the touch-as-right-click override in `overrides/mouse.talon` complements it.

The design is staged with decay:

- A list of duration thresholds (`thresholds = [0.6, 0.45, 0.3, 0.18, 0.1]`) governs how long a hiss must be to count as a click. The first click after a quiet period requires the longest hiss (0.6s); each successful click advances to a more sensitive stage.
- `decay_times` drops the stage back over time without use (60s, 30s, 15s, 3s).
- `max_hiss_dur = 1.2s` rejects hisses too long to be intentional.
- `require_mouse_move = True` rejects clicks when the mouse hasn't moved since the last action, preventing repeat-fires in the same spot from a sustained noise.

Net effect: deliberate clicks while actively pointing are fast; stray hisses during idle conversation are unlikely to fire. Adjust the threshold and decay arrays if false positives or false negatives become a problem.

### `key_hold.py`
Auto-repeating keypress with start/release semantics, adapted from Andreas Arvidsson's setup. Three actions:

- `key_hold(key, max_presses=256, repeat_rate="16ms", repeat_delay="256ms")` — begins repeating `key` after `repeat_delay`, at `repeat_rate`, up to `max_presses` times.
- `key_release(key)` — stops one key.
- `release_all_keys()` — stops all. Called by `^stop$` in `general.talon`.

### `fill.talon`
Fill-in-the-blank commands for fixed inserts. Two main patterns: user-name commands like `username {github}: insert("...")`, and `pathname {user.pathnames}: insert(pathnames)` for inserting paths from the `pathnames` list in `lists/`.

### `ssh.talon`
Work-specific `ssh ...` shortcuts to internal hosts.

## External prerequisites

The screenshot and mic-selection commands rely on shell scripts under `$HOME/bin/`: `screenshot`, `select_mic`, `take_note`, `take_context`. These must exist on any machine where the corresponding voice commands are used. **TODO: link to or document those scripts somewhere.**

## Open TODOs

- Rewrite or remove the `pactl`-based volume/mute actions in `general.py`.
- Document the misrecognition history behind the `(comma|Komma|item)` alias.
- Document or link the `$HOME/bin/` scripts that several actions depend on.
