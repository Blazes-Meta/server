import os
import shutil
from pathlib import Path

def delete_ignored_items(gitignore_path=".gitignore"):
    cwd = Path.cwd()
    if not (cwd / gitignore_path).exists():
        print(f"{gitignore_path} nicht gefunden.")
        return

    with open(gitignore_path, "r", encoding="utf-8") as f:
        patterns = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for pattern in patterns:
        for path in cwd.glob(pattern):
            try:
                if path.is_dir():
                    shutil.rmtree(path)
                    print(f"Ordner gelöscht: {path}")
                elif path.is_file():
                    path.unlink()
                    print(f"Datei gelöscht: {path}")
            except Exception as e:
                print(f"Fehler beim Löschen von {path}: {e}")

if __name__ == "__main__":
    delete_ignored_items()
