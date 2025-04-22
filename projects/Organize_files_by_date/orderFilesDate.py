import shutil
import platform
from pathlib import Path
from datetime import datetime

class orderFiles():
    def __init__(self, dir, order_by):
        self.dir = Path(dir)
        self.order_by = order_by.upper()
        self.allFiles = self.countFiles()

    def countFiles(self):
        try:
            all_files = [f for f in self.dir.iterdir() if f.is_file()]
            return all_files
        except Exception as e:
            print(f"ERROR: {e}")
            return []

    def getCMDate(self, file_path):
        try:
            if not file_path.exists():
                raise FileNotFoundError(f"File '{file_path}' not found")

            mod_date = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
            crt_date = None
            system = platform.system()

            if system == "Windows":
                crt_date = datetime.fromtimestamp(file_path.stat().st_ctime).strftime('%Y-%m-%d')
            elif system == "Darwin":  # macOS
                crt_date = datetime.fromtimestamp(file_path.stat().st_birthtime).strftime('%Y-%m-%d')
            else:
                crt_date = mod_date  # Linux doesn't store creation date

            return [crt_date, mod_date]
        except Exception as e:
            print(f"Date ERROR: {e}")
            return [None, None]

    def copyFilesByDate(self):
        for f in self.allFiles:
            dates = self.getCMDate(f)
            date = dates[1] if self.order_by == "M" else dates[0]
            if not date:
                continue
            dest_folder = self.dir / date
            dest_folder.mkdir(exist_ok=True)
            shutil.copy(f, dest_folder / f.name)
            print(f"Copied '{f.name}' to folder '{dest_folder}'")

if __name__ == "__main__":
    folder_path = r""  # << change path
    ordenador = orderFiles(folder_path, "c")  # "m" to modification date, "c" to creation
    ordenador.copyFilesByDate()
