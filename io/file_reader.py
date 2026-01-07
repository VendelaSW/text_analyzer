from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def select_file() -> Path | None:
    root = tk.Tk()
    root.withdraw() # Hide main window

    filename = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Textfiles", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        return Path(filename)
    return None

def read_text(file_path: Path) -> str:  
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


