import os
from fileFormats import file_types
import moveFiles
import shutil
from pathlib import Path

downloads_folder_path = str(Path.home() / "Downloads")
downloaded_files = os.listdir(downloads_folder_path)

def func():
    for file in downloaded_files:
        file_path = os.path.join(downloads_folder_path, file)
        
        if os.path.isfile(file_path):
            for file_type, file_format in file_types.items():
                destinationfolder_path = os.path.join(downloads_folder_path, file_type)
                if file.endswith(file_format):
                    moveFiles.to_folder(file_path, file_type)
                    break
            else:
                if file.startswith("Clic k me to organize files"):
                    continue
                try:
                    destinationfolder_path = os.path.join(downloads_folder_path, 'misc')
                    shutil.move(file_path, destinationfolder_path)
                    print(f"File '{file_path}' moved to '{destinationfolder_path}'.")
                except Exception as e:
                    print(f"Error moving the file: {e}")
        else:
            print(f"Skipping: {file}")
