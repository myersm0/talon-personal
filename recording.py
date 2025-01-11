import subprocess
import os
from talon import Module, Context

mod = Module()
mod.mode("recording", desc="Highly reduced mode to disable Talon speech while dictating notes")

@mod.action_class
class Actions:
    def run_external_command(program: str):
        """run an external command in a small Terminal.app window that closes when done"""
        script = f"""
        tell application "Terminal"
            activate
            do script "{program}; exit"
            set bounds of front window to {100, 100, 400, 200} -- left, top, right, bottom
        end tell
        """
        subprocess.run(["osascript", "-e", script], check=True)



