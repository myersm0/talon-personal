
from talon import Module, Context

mod_long = Module()
mod_long.mode("long", desc="Mode for longer speech timeout")

mod_recording = Module()
mod_recording.mode("recording", desc="Highly reduced mode to disable Talon speech while dictating notes")

mod_meeting = Module()
mod_meeting.mode("meeting", desc="Highly reduced mode for Zoom calls")

mod_seek = Module()
mod_seek.mode("seek", desc="Mode for seeking while in tmux")

mod_mouse = Module()
mod_mouse.mode("mouse", desc="Mode for mousing")
