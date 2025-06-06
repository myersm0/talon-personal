import subprocess
import os
from talon import Module, Context, actions
from typing import List

mod = Module()

@mod.action_class
class Actions:
    def concatenate(strings: List[str]):
        """concatenate a list of strings into a single string"""
        return ''.join(strings)

    def optional_enter(cmd: str):
        """optionally insert an `enter` keypress"""
        if cmd == "go":
            actions.key("enter")
        else:
            actions.key("space")

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

    def volume_down():
        """lower volume by five percent"""
        try:
            subprocess.run("pactl set-sink-volume @DEFAULT_SINK@ -5%", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def volume_up():
        """increase volume by five percent"""
        try:
            subprocess.run("pactl set-sink-volume @DEFAULT_SINK@ +5%", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def mute():
        """mute the volume"""
        try:
            subprocess.run("pactl set-sink-mute @DEFAULT_SINK@ 1", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def unmute():
        """unmute the volume"""
        try:
            subprocess.run("pactl set-sink-mute @DEFAULT_SINK@ 0", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def take_screenshot():
        """take a screenshot"""
        try:
            username = subprocess.run("whoami", shell=True, check=True, capture_output=True, text=True).stdout.strip()
            subprocess.run(f"/Users/{username}/bin/screenshot", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def set_default_mic():
        """set the default microphone, with a fallback"""
        try:
            username = subprocess.run("whoami", shell=True, check=True, capture_output=True, text=True).stdout.strip()
            subprocess.run(f'/Users/{username}/bin/select_mic "Shure MVX2U" "Samson Q9U" "Wireless PRO RX" "MacBook Pro Microphone"', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

    def set_builtin_mic():
        """set the microphone to my MacBook's built-in"""
        try:
            username = subprocess.run("whoami", shell=True, check=True, capture_output=True, text=True).stdout.strip()
            subprocess.run(f'/Users/{username}/bin/select_mic "MacBook Pro Microphone"', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")

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



