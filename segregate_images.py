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
    os.makedirs(os.path.join(folder_path, "1.5"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.333333333"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.25"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.4"), exist_ok=True)

    # Define the aspect ratio thresholds and corresponding folder names
    aspect_ratio_folders = {
        0.666666667: "0.666666667",
        0.75: "0.75",
        0.80: "0.80",
        0.714285714: "0.714285714",
        1: "1",
        1.25: "1.25",
        1.333333333: "1.333333333",
        1.5: "1.5",
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

            # Use shutil.move to move the file to the respective aspect ratio folder
            for threshold in sorted(aspect_ratio_folders.keys()):
                if aspect_ratio <= threshold:
                    new_file_path = os.path.join(folder_path, aspect_ratio_folders[threshold], file_name)
                    shutil.move(file_path, new_file_path)
                    break

