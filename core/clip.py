import os
import time
from talon import Module, actions, clip, ui

mod = Module()

@mod.action_class
class Actions:
    def save_selected_text_to_file():
        """Save selected text from browser to a file with a timestamp"""
        selected_text = actions.edit.selected_text() or clip.text()
        selected_from = ui.active_window().title
        text_to_paste = f"# source: {selected_from}\n{selected_text}"

        if not selected_text:
            actions.app.notify("No text selected")
            return

        timestamp = time.strftime("%Y%m%d_%H-%M-%S")
        folder_path = os.environ["CLIPS_DIR"]
        os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(folder_path, f"{timestamp}.txt")

        with open(file_path, "w") as f:
            f.write(text_to_paste)

        actions.app.notify(f"Text saved to {file_path}")

