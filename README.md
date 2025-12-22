# Desktop Organiser 🗂️

A Python-based desktop automation tool that organizes files on your desktop into categorized folders based on file types.  
The project supports both **Dry Run** (preview changes) and **Actual Run** modes, ensuring safety and control before execution.

---

## 📌 Features

- Automatically organizes desktop files by extension (PDFs, Images, Docs, Videos, etc.)
- **Dry Run mode** to preview actions without moving files
- **Run mode** to apply the organization
- Simple and lightweight Python script
- Packaged executable support using PyInstaller
- Prevents overwriting and handles existing folders safely

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** OS, shutil, argparse  
- **Packaging:** PyInstaller  


---

## 🚀 How It Works

1. Scans the desktop directory
2. Identifies file types using extensions
3. Creates folders if they don’t exist
4. Moves files into their respective folders  
   *(or just displays actions in Dry Run mode)*

---

## ▶️ Usage

### 🔍 Dry Run (Recommended First)
```bash
python Desktop_Organizer_DryRun.py
```

### 🔍 Actual Run
```bash
python Desktop_Organizer_Run.py
