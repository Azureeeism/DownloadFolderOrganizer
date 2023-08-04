import os
from fileFormats import file_types
import moveFiles
import shutil

DOWNLOADSFOLDER = r'C:\Users\LENOVO IP\Downloads'

files = os.listdir(DOWNLOADSFOLDER)

for file in files:
    file_path = os.path.join(DOWNLOADSFOLDER, file)
    if os.path.isfile(file_path):
        for file_type, extensions in file_types.items():
            if file.endswith(extensions):
                moveFiles.to_folder(file_path, file_type)
                break
            else:
                if file.startswith("Click me to organize files"):
                    break
                try:
                    destinationfolder_path = os.path.join(DOWNLOADSFOLDER + r'\misc')
                    shutil.move(file_path, destinationfolder_path)
                    print(f"File '{file_path}' moved to '{destinationfolder_path}'.")
                    break
                except Exception as e:
                    print(f"Error moving the file: {e}")
                    break
    else:
        print(f"Skipping: {file}")