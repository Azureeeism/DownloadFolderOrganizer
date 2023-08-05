import os
import shutil

def to_folder(source_file, destination_folder):

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    try:
        shutil.move(source_file, destination_folder)

        print(f"File '{source_file}' moved to '{destination_folder}'.")

    except Exception as e:
        print(f"Error moving the file: {e}")
