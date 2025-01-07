import subprocess
import os
from talon import Module, Context

mod = Module()
mod.mode("recording", desc="Highly reduced mode to disable Talon speech while dictating notes")

@mod.action_class
class Actions:
	def run_external_command(program: str):
		"""run an external command"""
        username = subprocess.run("whoami", shell=True, check=True, capture_output=True, text=True).stdout.strip()
		command = f"gnome-terminal --geometry=40x5+100+100 -- bash -c '{program}'"
		process = subprocess.Popen(f"/Users/{username}/bin/{command}", shell=True)
		process.wait()



