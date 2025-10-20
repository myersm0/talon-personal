app: /gimp/i
-

# -------------------------
# PROJECT MANAGEMENT
# -------------------------

project new:
	key(cmd-n)

project open:
	key(cmd-o)

project save:
	key(cmd-s)

project save as:
	key(shift-cmd-s)

project export:
	key(shift-cmd-e)

project close:
	key(cmd-w)

project quit:
	key(cmd-q)

undo:
	key(cmd-z)

redo:
	key(shift-cmd-z)

# -------------------------
# LAYER CONTROL
# -------------------------

layer new:
	key(shift-cmd-n)

layer duplicate:
	key(cmd-shift-d)

layer delete:
	key(delete)

layer merge down:
	key(cmd-m)

layer anchor:
	key(cmd-h)

layer scale:
	key(shift-cmd-t)

layer crop to selection:
	key(shift-cmd-c)

layer to image size:
	key(shift-cmd-i)

layer transparency add alpha:
	key(shift-cmd-a)

layer mask add:
	key(cmd-l)

layer mask apply:
	key(cmd-shift-l)

layer mask delete:
	key(shift-cmd-x)

# -------------------------
# SELECTIONS
# -------------------------

select all:
	key(cmd-a)

select none:
	key(shift-cmd-a)

select invert:
	key(cmd-i)

select grow:
	key(shift-cmd-g)

select shrink:
	key(shift-cmd-s)

select border:
	key(shift-cmd-b)

select feather:
	key(shift-cmd-f)

select by color:
	key(shift-o)

# -------------------------
# TOOLS
# -------------------------

tool move:
	key(m)

tool crop:
	key(shift-c)

tool select rectangle:
	key(r)

tool select ellipse:
	key(e)

tool select free:
	key(f)

tool select fuzzy:
	key(u)

tool color picker:
	key(o)

tool paintbrush:
	key(p)

tool pencil:
	key(n)

tool eraser:
	key(shift-e)

tool clone:
	key(c)

tool heal:
	key(h)

tool gradient:
	key(g)

tool bucket fill:
	key(shift-b)

tool text:
	key(t)

tool zoom:
	key(z)

tool measure:
	key(shift-m)

# -------------------------
# COLORS AND ADJUSTMENTS
# -------------------------

color invert:
	key(cmd-i)

color desaturate:
	key(shift-cmd-u)

color balance:
	key(shift-cmd-b)

color curves:
	key(shift-cmd-c)

color levels:
	key(cmd-l)

color brightness contrast:
	key(cmd-b)

color hue saturation:
	key(cmd-u)

color threshold:
	key(cmd-t)

# -------------------------
# VIEW AND ZOOM
# -------------------------

zoom in:
	key(cmd-plus)

zoom out:
	key(cmd-minus)

zoom fit image:
	key(cmd-shift-j)

zoom one hundred:
	key(cmd-1)

view fullscreen:
	key(f11)

view show grid:
	key(shift-cmd-g)

view snap to grid:
	key(shift-cmd-s)

view rulers:
	key(shift-cmd-r)

view guides:
	key(shift-cmd-g)

toggle dockable dialogs:
	key(tab)

# -------------------------
# IMAGE OPERATIONS
# -------------------------

image scale:
	key(shift-cmd-s)

image crop to content:
	key(shift-cmd-c)

image duplicate:
	key(cmd-d)

image flatten:
	key(shift-cmd-f)

image mode rgb:
	key(shift-cmd-r)

image mode grayscale:
	key(shift-cmd-g)

image mode indexed:
	key(shift-cmd-i)

image canvas size:
	key(shift-cmd-z)

# -------------------------
# PATHS AND MASKS
# -------------------------

path new:
	key(shift-cmd-n)

path stroke:
	key(shift-cmd-s)

path selection:
	key(shift-cmd-p)

mask quick toggle:
	key(shift-q)

# -------------------------
# SHORTCUT UTILITIES
# -------------------------

show shortcuts:
	key(shift-cmd-k)

show preferences:
	key(cmd-comma)

toggle toolbox:
	key(shift-t)

toggle layers dialog:
	key(shift-l)

toggle brushes dialog:
	key(shift-b)

toggle history dialog:
	key(shift-h)
