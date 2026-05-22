# overrides/

Customizations to lists, settings, and commands that originate in `talon-community-opt-in`. Every file here is gated by `tag: user.my_overrides`, declared in `my_overrides.py` and asserted from `environment/` (see that directory's README). The tag must be asserted on every machine for the overrides to take effect.

## Files

### `my_overrides.py`
Declares the `user.my_overrides` tag. No logic of its own.

### `letter.talon-list`
Replaces the community alphabet (air, bat, cap, ...) with the NATO phonetic alphabet (alpha, bravo, Charlie, ...). Full NATO mapping `alpha → a` through `Zulu → z`. The exception to NATO standard is `sienna` for "s" instead of `sierra`; the reason is that I found `sierra` was too easily misrecognized as `zero`.

### `special_key.talon-list`
Key-name overrides:

- `enter`, `carriage`, `snap` all map to `keypad_enter`.
- `delete` maps to `backspace`; the forward-delete key has no spoken form here.
- Shorthand additions: `chase` for space (reduces recognition conflicts compared to `space`), `complete` for tab.

### `code_formatter.talon-list`
Formatter renames and aliases relative to upstream:

- `camel` → `camel case` (less prone to misrecognition)
- `dub string` → `single string`, and `string` is remapped to `DOUBLE_QUOTED_STRING` instead of upstream's `SINGLE_QUOTED_STRING`. Net effect: "string" gives double quotes, "single string" gives single quotes. This is the inverse of upstream and matches the "double is default" convention also used in `keys.py`.
- `hammer` → `classname`, with `David` as an additional alias. Reason: I found `hammer` being frequently misrecognized with `camel`.

### `keys.py`
Overrides `user.punctuation` and `user.symbol_key`. Two themes:

1. **Double quote is the default for "quote"**, consistent with `code_formatter.talon-list`'s `string`.
2. **Disambiguating suffixes** to avoid misrecognition: several single-word punctuation names get a `" sign"` appended (e.g. `percent sign`, `hash sign`, `dollar sign`, `at sign`, `caret sign`). The motivating case was "percent" being recognized when "press enter" was spoken; appending "sign" makes it more distinguishable. Similarly, `curly` was renamed to `curly brace`.

### `delimiter_pair.talon-list`
Defines pairs for the `<user.delimiter_pair>` capture: `round`, `box`, `diamond`, `curly braces`, plus four pre-escaped variants (`escaped quad`, `escaped twin`, `escaped round`, `escaped box`).

### `word_formatter.talon-list`
Removes three upstream word formatters that I never used which were routinely misrecognized:

- `trot` → `TRAILING_SPACE`
- `proud` → `CAPITALIZE_FIRST_WORD`
- `leap` → `TRAILING_SPACE,CAPITALIZE_FIRST_WORD`

`trot` in particular was the most frequent offender. The remaining entry is `word: NOOP`.

### `mouse.talon`
Swaps the `touch` action (used with eye tracking) to right-click instead of upstream's left-click. Left-click is bound to a hiss sound elsewhere in the setup, so the touch gesture is freed up for a different role.

### `settings_command.talon` / `settings_dictation.talon`
Set `speech.timeout` to 0.25s in command mode and 1.0s in dictation mode. Both are gated by `not mode: user.long` — there is a `user.long` mode defined elsewhere in `talon-personal/` with its own (presumably longer) timeout policy.

### `symbols_deprecated.talon`
`inside quotes` / `inside string` insert between double quotes; `inside single quotes` inserts between single quotes. The filename suggests these were preserved from a community file that was deprecated or removed upstream.
