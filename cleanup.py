import shutil
from pathlib import Path
import fnmatch
import pathspec

exclude = [".vscode"]

def delete_ignored_items(gitignore_path=".gitignore"):
    cwd = Path.cwd()
    gi_file = cwd / gitignore_path
    if not gi_file.exists():
        print(f"{gitignore_path} nicht gefunden.")
        return

    with open(gi_file, "r", encoding="utf-8") as f:
        spec = pathspec.PathSpec.from_lines("gitwildmatch", f)

    # Alle Pfade einmal erfassen
    all_paths = sorted(cwd.rglob("*"), key=lambda p: len(p.parts), reverse=True)

    for path in all_paths:
        rel_path = str(path.relative_to(cwd))

        # Ausnahmen überspringen
        if any(fnmatch.fnmatch(rel_path, pat) for pat in exclude):
            continue

        # Nur löschen, wenn .gitignore-Muster passt
        if spec.match_file(rel_path):
            try:
                if path.is_file():
                    path.unlink()
                    print(f"Datei gelöscht: {rel_path}")
                elif path.is_dir():
                    shutil.rmtree(path, ignore_errors=False)
                    print(f"Ordner gelöscht: {rel_path}")
            except Exception as e:
                print(f"Fehler beim Löschen von {rel_path}: {e}")

if __name__ == "__main__":
    # Beispiel: alles aus .gitignore löschen außer logs/ und .env
    delete_ignored_items()
