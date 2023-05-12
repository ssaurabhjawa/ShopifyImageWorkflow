import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
from PIL import Image


def segregate_images_by_aspect_ratio():
    # Ask user to select the folder containing images to be segregated
    root = Tk()
    root.withdraw()
    folder_path = askdirectory(title="Select Folder Containing Images to be Segregated")

    # Create directory for each aspect ratio
    os.makedirs(os.path.join(folder_path, "0.80"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.3"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.25"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.4"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.5"), exist_ok=True)




    # Define aspect ratio ranges and create folders
    aspect_ratios = {
        (0.0, 0.7): '0.67',
        (0.71, 0.74): '0.71',
        (0.75, 0.79): '0.75',
        (0.8, 0.9): '0.8',
        (1, 1.24): '1.0',
        (1.25, 1.32): '1.25',
        (1.33333, 1.399): '1.333',
        (1.4, 1.49): '1.4',
        (1.5, 2): '1.5',
    }

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            file_path = os.path.join(folder_path, file_name)

            # Skip the file if it's being used by another process
            try:
                with Image.open(file_path) as img:
                    aspect_ratio = img.size[0] / img.size[1]
            except (PermissionError, OSError):
                print(f"{file_name} is being used by another process, skipping...")
                continue

            # Use aspect_ratios dictionary to determine the appropriate folder
            for range_, folder in aspect_ratios.items():
                if range_[0] <= aspect_ratio < range_[1]:
                    new_folder_path = os.path.join(folder_path, folder)
                    if not os.path.exists(new_folder_path):
                        os.mkdir(new_folder_path)

                    # Use shutil.move to move the file to the respective folder
                    new_file_path = os.path.join(new_folder_path, file_name)
                    shutil.move(file_path, new_file_path)
                    print(f"Moved {file_name} to {new_folder_path}")
                    break
            else:
                print(f"No appropriate folder found for {file_name}")