import os
import shutil
DOWNLOADSFOLDER = r'C:\Users\LENOVO IP\Downloads'

def to_folder(source_file, destination_folder):

    destinationfolder_path = os.path.join(DOWNLOADSFOLDER, destination_folder)

    if not os.path.exists(destinationfolder_path):
        os.makedirs(destinationfolder_path)

    try:
        shutil.move(source_file, destinationfolder_path)

        print(f"File '{source_file}' moved to '{destinationfolder_path}'.")

    except Exception as e:
        print(f"Error moving the file: {e}")
