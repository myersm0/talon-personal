import subprocess
from talon import Module

mod = Module()

@mod.action_class
class Actions:
    def networking_on():
        """turn networking on"""
        try:
            subprocess.run("nmcli networking on", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def networking_off():
        """turn networking off"""
        try:
            subprocess.run("nmcli networking off", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")
