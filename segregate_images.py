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
    os.makedirs(os.path.join(folder_path, "0.666666667"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "0.75"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "0.80"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "0.714285714"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.333333333"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.25"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.4"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.5"), exist_ok=True)




    # Define aspect ratio ranges and create folders
    aspect_ratios = {
        (0.0, 0.9): '0.8',
        (0.9, 1.1): '1.0',
        (1.1, 1.4): '1.3',
        (1.4, 1.6): '1.5',
        (1.6, 1.8): '1.8',
        (1.8, float('inf')): '2.0'
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