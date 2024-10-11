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
            subprocess.run("screenshot", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            # Handle error (optional)
            print(f"Command failed with error: {e}")


