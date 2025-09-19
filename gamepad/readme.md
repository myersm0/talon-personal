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
|L3|||long mode|long mode|
|R3|||long mode|long mode|
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

## Long mode (L3/R3 held)
- If already in long mode, pressing other stick → focus next
- Speech enabled while held

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
|L-stick||||vim movement (hjkl/wb)|
|R-stick||||arrow movement|

## Safari
|Key|Tap|Short|Long|Hold|
|---|---|---|---|---|
|D-pad|arrow keys (on release)||||
|North|enter||||
|South|click||||
|West|escape||||
|East|escape||||

## Julia REPL
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
|R3||toggle mute|||
|Select||cmd-q|||
|Start|screenshot||||

## Special modes
- **Meeting mode**: L3/R3 enable/disable speech without long mode
- **Recording mode**: East button exits recording and optionally wakes speech
- **Seek mode**: Terminal navigation with different key mappings
