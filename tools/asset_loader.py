import sys, os
from pathlib import Path

ROOT = Path(__file__).parent.parent
ASEPRITE_FOLDER = ROOT / "aseprite"
DATA_ASSETS_TEXTURES = ROOT / "data" / "assets" / "textures"

DATA_ASSETS_TEXTURES.mkdir(parents=True, exist_ok=True)

if ASEPRITE_FOLDER.exists() and DATA_ASSETS_TEXTURES.exists():
    _SUCCESS = False
    total_files = len(list(ASEPRITE_FOLDER.iterdir()))
    files_did = 0
    for file in ASEPRITE_FOLDER.iterdir():
        if file.suffix in [".png", ".jpg", ".jpeg"]:
            destination = DATA_ASSETS_TEXTURES / file.name
            destination.write_bytes(file.read_bytes()) # Overwrite the file if it already exists
            files_did += 1
            print("Loading assets: {}/{} files copied.".format(files_did, total_files), end="\r")
        else: total_files -= 1
    _SUCCESS = True
    
    if _SUCCESS:
        print("Assets loaded to {} successfully.\nLoaded {}/{} files.".format(DATA_ASSETS_TEXTURES, files_did, total_files))
    else:
        print("Failed to load assets to {}.".format(DATA_ASSETS_TEXTURES))
else:
    print("Failed to load assets to {}. Check if the aseprite folder exists.".format(DATA_ASSETS_TEXTURES))