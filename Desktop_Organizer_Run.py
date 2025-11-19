#!/usr/bin/env python3
"""
Desktop File Organizer - ACTUAL VERSION
Moves files into folders automatically.
"""

import os
import pathlib
import shutil
import tkinter as tk
from tkinter import messagebox

# --- Categories ---
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def organize_files():
    # Automatically detect real Desktop path (handles OneDrive too)
    import pathlib
desktop = str(pathlib.Path.home() / "Desktop")
if not os.path.exists(desktop):
    possible = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    if os.path.exists(possible):
        desktop = possible

    ext_to_cat = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}

    moved, skipped = 0, 0

    for item in os.listdir(desktop):
        src = os.path.join(desktop, item)
        if os.path.isfile(src):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            if ext in ext_to_cat:
                category = ext_to_cat[ext]
                dest_folder = os.path.join(desktop, category)
                dest_path = os.path.join(dest_folder, item)

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder, exist_ok=True)

                shutil.move(src, dest_path)
                moved += 1
            else:
                skipped += 1

    messagebox.showinfo(
        "Organization Complete",
        f"Desktop organized successfully!!\n\nFiles moved: {moved}\nFiles skipped: {skipped}"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() 
    organize_files()
