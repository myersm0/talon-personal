import os
import time
from talon import Module, actions, clip

mod = Module()

@mod.action_class
class Actions:
    def save_selected_text_to_file():
        """Save selected text from browser to a file with a timestamp"""
        selected_text = actions.edit.selected_text() or clip.text()

        if not selected_text:
            actions.app.notify("No text selected")
            return

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        folder_path = os.environ["CLIPS_DIR"]
        os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(folder_path, f"{timestamp}.txt")

        with open(file_path, "w") as f:
            f.write(selected_text)

        actions.app.notify(f"Text saved to {file_path}")

