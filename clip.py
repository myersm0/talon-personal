import os
import time
from talon import Module, actions, clip

mod = Module()

@mod.action_class
class Actions:
    def save_selected_text_to_file():
        """Save selected text from browser to a file with a timestamp"""
        # Get the selected text from clipboard
        selected_text = actions.edit.selected_text() or clip.text()

        if not selected_text:
            actions.app.notify("No text selected")
            return

        # Create timestamped filename
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        folder_path = os.path.expanduser("~/contents/083e4b/")
        os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(folder_path, f"{timestamp}.txt")

        # Write the selected text to the file
        with open(file_path, "w") as f:
            f.write(selected_text)

        actions.app.notify(f"Text saved to {file_path}")

