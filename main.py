import os
from fileFormats import file_types
import moveFiles

downloadsFolder = r'C:\Users\LENOVO IP\Downloads'

files = os.listdir(downloadsFolder)

for file in files:
    file_path = os.path.join(downloadsFolder, file)
    if os.path.isfile(file_path):
        for file_type, extensions in file_types.items():
            if file.endswith(extensions):
                moveFiles.to_folder(file_path, file_type)
                break
            else:
                if file.startswith("Click me to organize files"):
                    break
                else:
                    moveFiles.to_folder(file_path, r'\Misc')
                    break
    else:
        print(f"Skipping: {file}")