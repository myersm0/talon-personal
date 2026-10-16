# Gamepad mappings

The controller is a DualSense Edge, read by InputConfig rather than Talon. InputConfig handles everything that means the same in every app: both sticks move the mouse, L2 and R2 scroll with pressure-scaled speed, and a 2 s PS hold is the emergency stop. Every other button is sent to Talon as a private key, held for exactly as long as the button is, and `gamepad.talon` turns those keys into the button names below.

## Key scheme
|Control|Key from InputConfig|Talon|
|---|---|---|
|Touchpad press|not sent|handled in InputConfig|
|Mute|F7|speech toggle (`modes/push_to_talk.talon`)|
|D-pad left, up, right, down|F13, F14, F15, F16|`dpad_left`, `dpad_up`, `dpad_right`, `dpad_down`|
|West, north, east, south|F17, F18, F19, F20|`west`, `north`, `east`, `south`|
|Create, Options|shift-F13, shift-F14|`select`, `start`|
|L1, R1|shift-F15, shift-F16|`left_shoulder`, `right_shoulder`|
|Back paddle left, right|shift-F17, shift-F18|`left_paddle`, `right_paddle`|
|Fn left, right|shift-F19, shift-F20|`left_function`, `right_function`|
|Sticks, L2, R2, PS|not sent|handled in InputConfig|
|Stick clicks|unbound||

The paddles are only reported in the Edge's default profile (Fn + Triangle). Talon still receives native gamepad events while the Edge is wired, so no `gamepad()` matcher may exist anywhere in the user directory: it would double every press.

## Press durations
- Tap: < 0.3s
- Short: 0.3-0.8s
- Long: > 0.8s
- Hold: continuous (with autorelease at 0.8s for face buttons, Create, Options and shoulders)

## Default (no mode) behavior
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|arrow keys||||
|North (Y)|space||||
|South (A)|enter||||
|West (X)|backspace||||
|East (B)|dot||||
|Create|cmd-w|cmd-q|||
|Options|cmd-t|cmd-n|cmd-shift-n||
|L1|ctrl-shift-tab||||
|R1|ctrl-tab||||
|Left paddle||||window picker (see below)|
|Right paddle||||app picker (see below)|
|Left Fn|push to talk||||
|Right Fn|push to talk||||

## Mouse mode
Previously entered by stick movement, which Talon no longer sees; nothing enters it at the moment. The table stays in `mouse.py` until it's decided whether InputConfig can signal stick deflection with a key.

|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|mouse jump (halve distance to edge)||||
|North (Y)|cmd+click||||
|South (A)||||drag (no autorelease)|
|West (X)|shift+click||||
|East (B)|right click||||

## Pickers (paddles held)
The right paddle shows running apps, most recently used first; the left paddle shows the current app's windows, in the order macOS reports them (expected front to back), skipping untitled and minimized ones. Either opens with the second entry highlighted and focuses the highlighted entry on release, so a quick tap is "focus last app" or "focus last window". Implemented in `picker.py` as one Talon imgui list; app recency comes from an `app_activate` callback.

While a picker is showing, these buttons are intercepted before any context bindings:

|Key|Action|
|---|---|
|D-pad left / up, L1|move highlight up|
|D-pad right / down, R1|move highlight down|

## Long mode (voice: "long mode")

|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|window/focus navigation||||
|North|window next||||
|South|window last||||
|West|focus last||||
|East|focus last||||
|Create|set dummy mike||||
|Options|set default mike||||

## Terminal
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|North|space|yank to end|yank line||
|South|enter||put||
|West|backspace|del to end|del line||
|East|ctrl-c|change to end|change line||
|Create|exec line||||
|Options|exec block||||
|L1|zellij previous tab||||
|R1|zellij next tab||||

## Terminal + long mode
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|tmux pane navigation (ctrl-a + hjkl; stale since zellij)||||
|L1|undo (esc u)||||
|R1|redo (esc ctrl-r)||||

## Safari
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|arrow keys (on release)||||
|North|enter||||
|South|click||||
|West|escape||||
|East|escape||||

## kenburns-renderer (`julia.py`, app `/kbr/i`)
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad left/right|arrow keys|||hold|
|D-pad up/down|arrow keys (on release)||||
|North|space||||
|South|enter||||
|East|q||||
|L1|ctrl-pagedown||||
|R1|ctrl-pageup||||

## Claude Desktop (`claude.py`)
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|arrow keys||||
|South|newline (shift-enter)|newline|send (enter)||
|West|backspace|delete word|delete to line start||
|East|escape|stop response (cmd-.)|||
|North|space|focus input (cmd-shift-;)|||
|Create|cmd-w|cmd-q|||
|Options|new chat (cmd-shift-o)|search (cmd-k)|new window (cmd-n)||
|L1|previous Claude window (cmd-shift-`)||||
|R1|next Claude window (cmd-`)||||

Send is long-press only so it can't be confused with a newline. The east, north and Options chords come from third-party cheat sheets, not Anthropic docs; verify against the menu bar.

## Zoom
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|North||toggle mute|||
|Create||cmd-q|||
|Options|screenshot||||

## Special modes
- **Quiet mode** (`user.quiet`, see `modes/README.md`): gamepad stays live
- **Recording mode**: East button exits recording and optionally wakes speech
- **Seek mode**: Terminal navigation with different key mappings

## Architecture

InputConfig → key → `gamepad.talon` → `user.gamepad_button_down/up(button)` in
`gamepad.py` → ignores a down for a button already held (key repeat, stray
duplicates) and an up for a button not held, timestamps the press, schedules
an 800ms autorelease for buttons in `buttons_with_autorelease`, computes
`held ∈ {0,1,2}` on release, dispatches via
`getattr(actions.user, "gamepad_press_X" / "gamepad_release_X")`.

Per-context behavior lives in the small files (`general.py`, `terminal.py`,
etc.), each declared as a data table via `bindings.install(ctx, {...})`. The
`bindings` module supplies the binding helpers (`repeat_key`, `tap_key`,
`press_key`, `tap_keys`, `tap_call`, `by_hold`, `mimic_phrase`, `hold`). Anything
a context doesn't bind falls through to the module-level defaults in
`gamepad.py`, which implement gamepad-as-mouse behavior (drag on west/north,
right-click on east, etc.).

## Kill switch
InputConfig's preset toggle shortcut turns the sticks off if an axis ever sticks; the old F9 toggle in Talon is gone with the stick handling.
