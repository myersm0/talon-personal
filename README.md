# talon-personal

My custom [Talon Voice](https://talonvoice.com/) commands and configuration.

## Directories

- `apps/` — per-app command palettes (Terminal, Photoshop, Finder). See `apps/README.md`.
- `core/` — general commands plus Python utility modules: mic switching, screenshot, hiss-as-click, key auto-repeat, clip-selection-to-file. See `core/README.md`.
- `gamepad/` — gamepad button and thumbstick handling, including the gamepad-triggered `user.mouse` and `user.symbol` modes. **TODO: README pending.**
- `lists/` — talon-list definitions consumed by commands elsewhere: vim actions, Greek letters, project codes, common paths, formatter aliases, and so on. See `lists/README.md`.
- `modes/` — custom modes (long, recording, meeting, seek, mouse, symbol) and the voice commands that enter or exit them. See `modes/README.md`.
- `overrides/` — replacements and tweaks for upstream community files, all gated by the `user.my_overrides` tag. See `overrides/README.md`.

## Overview

- `lists/` populates the `{user.X}` captures consumed by commands in `apps/`, `core/`, and `modes/`.
- `core/general.py` exposes Python actions (`set_default_mic`, `run_external_command`, `release_all_keys`, `save_selected_text_to_file`, etc.) called from `core/general.talon`, `modes/recording.talon`, and other places that need a Python implementation.
- `modes/` declares modes that are read by `not mode: user.long` guards in `overrides/`, by per-mode behavior files in `modes/` itself, and by the `^...mode$` toggle commands.
- `overrides/` activates only when `user.my_overrides` is asserted. The asserter lives outside this repo, in `~/.talon/user/environment/`, and must include `tag(): user.my_overrides` on every machine — see the war story in `overrides/README.md`.
- `apps/terminal.talon` asserts `tag(): user.use_app_git`, opting into the upstream community fork's git commands inside terminal apps. That's a pattern available to any personal app file that wants to layer specific upstream features on top of its own commands.

## Conventions

**The `dont_go` idiom.** Most terminal commands that would otherwise press enter accept an optional `[{user.dont_go}]` suffix capture. Saying "but wait" or "then wait" leaves the constructed command on the prompt instead of executing it. Implementation in `core/general.py`; spoken forms in `lists/dont_go.talon-list`.

**NATO alphabet.** The default community alphabet (air, bat, cap, …) is replaced with NATO (alpha, bravo, Charlie, …) in `overrides/letter.talon-list`. Requires `user.my_overrides` to be asserted; otherwise the community default remains active and saying NATO words produces nothing.

**Inverted-polarity meeting mode.** Normal operation has speech on by default with F6 as push-to-mute. Meeting mode inverts: speech off by default, with F5 or gamepad L3 as push-to-talk. The polarity flip is what makes meeting mode safe on calls.

## License

See `LICENSE`.
