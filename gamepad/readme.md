# Gamepad mappings

## Press durations
- Tap: < 0.3s
- Short: 0.3-0.8s  
- Long: > 0.8s
- Hold: continuous (with autorelease except for triggers/sticks)

## Default (no mode) behavior
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|arrow keys||||
|North (Y)|space||||
|South (A)|enter||||
|West (X)|backspace||||
|East (B)|dot||||
|Select|cmd-w|cmd-q|||
|Start|cmd-t|cmd-n|cmd-shift-n||
|L1|ctrl-shift-tab||||
|R1|ctrl-tab||||
|L2||||scroll up|
|R2||||scroll down|
|L3||||push-to-talk (speech on while held)|
|R3||||app switcher (cmd held; see below)|
|L-stick||||mouse move (slow)|
|R-stick||||mouse move (fast)|

## Mouse mode (auto-activated by stick movement)
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|mouse jump (halve distance to edge)||||
|North (Y)|cmd+click||||
|South (A)||||drag (no autorelease)|
|West (X)|shift+click||||
|East (B)|right click||||
|*Other buttons*|same as default||||

## App switcher (R3 held)
Pressing R3 shows a list of running apps, most recently used first, with the previous app highlighted. Releasing R3 focuses the highlighted app, so a quick tap is "focus last". Implemented in `app_switcher.py` as a Talon imgui list; recency comes from an `app_activate` callback.

While R3 is held, these buttons are intercepted before any context bindings:

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
|Select|set dummy mike||||
|Start|set default mike||||
|L2|undo||||
|R2|redo||||

## Terminal
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|North|space|yank to end|yank line||
|South|enter||put||
|West|backspace|del to end|del line||
|East|ctrl-c|change to end|change line||
|Select|exec line||||
|Start|exec block||||
|L1|cmd-left (tab prev)||||
|R1|cmd-right (tab next)||||
|L2|go doc start||||
|R2|go doc end||||

## Terminal + long mode
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|tmux pane navigation (ctrl-a + hjkl)||||
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

## Julia
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad left/right|arrow keys|||hold|
|D-pad up/down|arrow keys (on release)||||
|North|space||||
|South|enter||||
|West|backspace||||
|East|q||||
|L1|ctrl-pagedown||||
|R1|ctrl-pageup||||

## Zoom
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|North||toggle mute|||
|Select||cmd-q|||
|Start|screenshot||||

## Special modes
- **Meeting mode**: L3 enables/disables speech (now the same as the default)
- **Quiet mode** (`user.quiet`, see `modes/README.md`): gamepad stays live; L3 does nothing because speech is already on
- **Recording mode**: East button exits recording and optionally wakes speech
- **Seek mode**: Terminal navigation with different key mappings

## Architecture

Voice/Talon → `gamepad.talon` → `user.gamepad_button_down/up(button)` in
`gamepad.py` → timestamps press, schedules 800ms autorelease for buttons in
`buttons_with_autorelease`, computes `held ∈ {0,1,2}` on release, dispatches via
`getattr(actions.user, "gamepad_press_X" / "gamepad_release_X")`.

Per-context behavior lives in the small files (`general.py`, `terminal.py`,
etc.), each declared as a data table via `bindings.install(ctx, {...})`. The
`bindings` module supplies the binding helpers (`repeat_key`, `tap_key`,
`press_key`, `tap_keys`, `tap_call`, `by_hold`, `mimic_phrase`, `hold`). Anything
a context doesn't bind falls through to the module-level defaults in
`gamepad.py`, which implement gamepad-as-mouse behavior (drag on west/north,
right-click on east, etc.).

## Stick safeguards
Some controllers, in some connection modes, report a stick axis as permanently deflected, which used to send the mouse running in one direction until Talon was killed. Three guards in `gamepad.py`:

- **Dead zone:** readings within 0.15 of center are ignored.
- **Arm on center:** a stick moves the mouse only after it has been seen at rest, so a stick stuck from the moment of connection never moves anything.
- **Stuck detection:** an identical off-center reading for 1.5 s disarms that stick (with a notification) until it returns to center.

**Kill switch:** F9 toggles all stick input off/on, in every mode (`kill_switch.talon`).
