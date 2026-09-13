import os
import zipfile

ZIP_FILENAME = "KONE-Elevator-AI.zip"
EXCLUDE_DIRS = {"node_modules", ".git", "dist", "venv", ".venv", "__pycache__", ".pytest_cache"}
EXCLUDE_EXTS = {".db", ".sqlite", ".sqlite3", ".pyc", ".zip"}
EXCLUDE_FILES = {"test_err.txt", "test_quick_api.py", "build.log", "startup_err.txt"}

def create_zip():
    count = 0
    total_bytes = 0
    with zipfile.ZipFile(ZIP_FILENAME, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for f in files:
                if f in EXCLUDE_FILES or any(f.endswith(ext) for ext in EXCLUDE_EXTS):
                    continue
                file_path = os.path.join(root, f)
                # Normalize zip path under folder KONE-Elevator-AI/
                arcname = os.path.join("KONE-Elevator-AI", os.path.relpath(file_path, "."))
                zf.write(file_path, arcname)
                count += 1
                total_bytes += os.path.getsize(file_path)

    zip_size = os.path.getsize(ZIP_FILENAME)
    print(f"ZIP Creation Complete!")
    print(f"Files included: {count}")
    print(f"Uncompressed Source Size: {total_bytes / (1024 * 1024):.2f} MB")
    print(f"ZIP Size: {zip_size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    create_zip()
