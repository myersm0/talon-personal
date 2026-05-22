# apps/

Per-app command palettes for the apps I use. Each file is gated by a Talon `app:` header — not by the `user.use_app_*` opt-in tag system used in `talon-community-opt-in/apps/`. Since I wrote these commands, I control their context directly; the opt-in plumbing isn't needed for my own work. The pattern is still available the other direction, though: a personal app file can *assert* an opt-in tag to enable upstream commands inside that app's context. `terminal.talon` does this with `tag(): user.use_app_git`.

## Files

### `finder.talon`
A single command: `go home` for cmd-shift-h.

### `photoshop.talon`
Self-explanatory.

### `terminal.talon`
The big one. Header is OR'd: `app: /terminal/i` and `app: /term/i`, so it activates for any terminal-named app (Terminal.app, iTerm2). Asserts `tag(): user.use_app_git`, which enables the opt-in fork's git commands inside the terminal.

Organized into sections by `##` comments:

- **virtual instruments** — launch Pianoteq and Organteq in `--serve` mode (used as standalone audio engines from external sequencers).
- **work project names** — `CCF {project} {project_qualifier}` constructs strings like `CCF_ADCPWI_ITK` from the `project` and `project_qualifier` lists.
- **slurm** — `cue stat`, `cue stat HCP`, `cue stat ADCP` for formatted `squeue` output.
- **misc** — unicode inserts, Greek inserts, `empty args`, `empty brackets`.
- **vim** — substantial: ex-mode commands, action+motion patterns using `vim_actions` and `vim_actions_long`, range-based substitutions, the `vim clear` highlight-clear hack (greps for a nonsense string), syntax-coloring toggle, scroll/look helpers (`look down`/`look up` peek the buffer by holding then reversing; `scroll up`/`scroll down` sustain).
- **zellij** — pane navigation (cardinal directions and ctrl-hjkl), pane creation, stack/eject, tab rename. Optionally prefixed with `[go|move|tmux]`.
- **bash** — the largest section: ls variants, git commit, rsync helpers, copy/mkdir, find, grep with optional flags from `grep_options`, sed, conda, history search, pbpaste, `array` for `"${var[@]}"` insertion, and more.
- **navigation helpers** — shortcuts for my `Clew.jl` and `bash-productivity` repos: `clew insert/search`, `goahead/gobehind`, `cdr/cdf/cdp`, `grab`, `recall`, `<digits> snap` / `snap <digits>` for entering a number and pressing enter.
- **personal note taker** — `log read` and `log write` for my note-taking tool.
- **ssh** — work hosts.
- **rust** — cargo build/test/run/run-binary, with and without `--release`.
- **ollama** — `ollama serve`

## Recurring patterns in `terminal.talon`

### The `dont_go` idiom
Most terminal commands that would normally press enter accept an optional `[{user.dont_go}]` capture and end with:

```
go = dont_go or "go"
user.optional_enter(go)
```

If you said "but wait" or "then wait" at the end of the command, this presses space and leaves the command on the prompt for further editing; otherwise it presses enter. Implementation lives in `core/general.py`; the spoken forms are in `lists/dont_go.talon-list`.

### Regex anchoring
Some standalone commands (vim mode operations, anything that auto-executes, scroll/look) use `^...$` anchors so partial matches in longer utterances don't fire them. Composable commands (those that combine with captures like `project`, `pathnames`, `dont_go`, or `vim_actions`) are unanchored so they can be chained.

### List composition
The file is a heavy consumer of `lists/`: `unicode`, `lower_greek`, `upper_greek`, `project`, `project_qualifier`, `unix_operators`, `unix_tools`, `vim_actions`, `vim_actions_long`, `pathnames`, `array_names`, `grep_options`, `dont_go`. See `lists/README.md` (TBD) for what each contains.

## External prerequisites

`terminal.talon` leans on a lot of off-Talon machinery that must exist on the machine for the commands to do anything useful:

- **Personal shell tools**: `goahead`, `gobehind`, `grab`, `recall`, `cdr`, `cdf`, `cdp`, `log`.
- **Shell env vars**: `$cpref` (chpc rsync prefix) and `$hpref` (shadow rsync prefix), set in shell rc files.
- **Versioned app paths**: Pianoteq and Organteq paths are pinned to `Pianoteq 9` and `Organteq 2`. **TODO: factor these out (list entry or glob) so version bumps don't break the commands.**
- **Work hosts and identities**: These will fail or worse on a personal machine; consider gating with `user.wustl`.

## Open TODOs

- Typos: `[lower|litte]` → `little`; `copy recusrive` → `recursive`.
- Fix `finder.talon` header to be case-insensitive.
- Resolve overlap (or lack thereof) between this file's ssh section and `core/ssh.talon`.
- Factor Pianoteq/Organteq paths out of the virtual instrument commands.
- Consider gating work-specific commands (ssh hosts, work project names, slurm helpers) on `user.wustl` so they don't pollute the personal-machine vocabulary. Most of these are inert on personal but the recognition surface is still active.
