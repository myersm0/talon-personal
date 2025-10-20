app: /logic pro/i
-

# -------------------------
# TRANSPORT AND PLAYBACK
# -------------------------

play:
	key(space)

stop:
	key(space)

record:
	key(r)

cycle on off:
	key(c)

rewind:
	key(comma)

forward:
	key(period)

return to start:
	key(return)

play from selection:
	key(ctrl-space)

metronome:
	key(k)

count in:
	key(shift-k)

replace mode:
	key(cmd-r)

loop playback:
	key(cmd-u)

toggle low latency mode:
	key(alt-l)

# -------------------------
# EDITING REGIONS AND NOTES
# -------------------------

region split:
	key(cmd-t)

regions join:
	key(cmd-j)

region mute:
	key(ctrl-m)

region solo:
	key(ctrl-s)

region duplicate:
	key(cmd-d)

region delete:
	key(delete)

quantize:
	key(q)

region normalize:
	key(ctrl-n)

region reverse:
	key(ctrl-r)

toggle automation:
	key(a)

toggle flex time:
	key(alt-f)

toggle flex pitch:
	key(ctrl-f)

# -------------------------
# TRACK CONTROLS
# -------------------------

new audio track:
	key(cmd-alt-a)

new software instrument track:
	key(cmd-alt-s)

track duplicate:
	key(cmd-d)

track delete:
	key(cmd-backspace)

track mute:
	key(m)

track solo:
	key(s)

track enable record:
	key(r)

tracks arm all:
	key(shift-r)

# -------------------------
# NAVIGATION AND SELECTION
# -------------------------

track next:
	key(down)

track previous:
	key(up)

region next:
	key(tab)

region previous:
	key(shift-tab)

(head|go to beginning):
	key(return)

(tail|go to end):
	key(fn-right)

go to bar:
	key(shift-g)

zoom in:
	key(cmd-right)

zoom out:
	key(cmd-left)

zoom to fit selection:
	key(z)

toggle smart zoom:
	key(ctrl-z)

horizontal zoom in:
	key(ctrl-right)

horizontal zoom out:
	key(ctrl-left)

# -------------------------
# VIEW TOGGLES AND WINDOWS
# -------------------------

toggle mixer:
	key(x)

toggle editor:
	key(e)

toggle piano roll:
	key(p)

toggle event list:
	key(d)

toggle step sequencer:
	key(ctrl-shift-s)

toggle score editor:
	key(cmd-3)

toggle track inspector:
	key(i)

toggle smart controls:
	key(b)

toggle library:
	key(y)

toggle browser:
	key(f)

toggle plugins:
	key(cmd-ctrl-p)

toggle mixer on right:
	key(shift-x)

open plugin window:
	key(cmd-shift-p)

open track stack:
	key(cmd-u)

# -------------------------
# MARKERS AND ARRANGEMENT
# -------------------------

marker create:
	key(alt-apostrophe)

marker next:
	key(ctrl-period)

marker previous:
	key(ctrl-comma)

marker delete:
	key(ctrl-delete)

marker rename:
	key(ctrl-shift-apostrophe)

create arrangement marker:
	key(cmd-shift-a)

# -------------------------
# MIXING AND AUTOMATION
# -------------------------

toggle automation:
	key(a)

read automation mode:
	key(ctrl-cmd-r)

write automation mode:
	key(ctrl-cmd-w)

touch automation mode:
	key(ctrl-cmd-t)

latch automation mode:
	key(ctrl-cmd-l)

toggle volume automation:
	key(ctrl-v)

toggle pan automation:
	key(ctrl-p)

show plugin automation:
	key(ctrl-a)

# -------------------------
# PROJECT MANAGEMENT
# -------------------------

project new:
	key(cmd-n)

project open:
	key(cmd-o)

project save:
	key(cmd-s)

save as:
	key(shift-cmd-s)

project close:
	key(cmd-w)

undo:
	key(cmd-z)

redo:
	key(shift-cmd-z)

project bounce:
	key(cmd-b)

export selection:
	key(shift-cmd-e)

# -------------------------
# TOOLS AND CURSORS
# -------------------------

pointer tool:
	key(t) ; key(t)

pencil tool:
	key(t) ; key(p)

eraser tool:
	key(t) ; key(e)

scissors tool:
	key(t) ; key(i)

glue tool:
	key(t) ; key(g)

mute tool:
	key(t) ; key(m)

fade tool:
	key(t) ; key(a)

marquee tool:
	key(t) ; key(r)

zoom tool:
	key(t) ; key(z)

automation select tool:
	key(t) ; key(x)

# -------------------------
# LEARNING AND UTILITY
# -------------------------

show help tags:
	key(shift-slash)

toggle quick help:
	key(shift-slash)

show key commands:
	key(alt-k)

toggle control bar:
	key(shift-cmd-7)

show inspector help:
	key(shift-question)
