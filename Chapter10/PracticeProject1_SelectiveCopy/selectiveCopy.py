import os
import shutil

def selective_copy(source_folder, destination_folder, file_extension):
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the folder tree
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            # Check if the file has the desired extension
            if filename.lower().endswith(file_extension.lower()):
                # Construct the full file path
                file_path = os.path.join(foldername, filename)
                # Copy the file to the destination folder
                shutil.copy(file_path, destination_folder)
                print(f'Copied {filename} to {destination_folder}')

# Example usage
source_folder = './Photos'  # Replace with your source folder path
destination_folder = './JPG_BackUp'  # Replace with your destination folder path
file_extension = '.jpg'  # Replace with the desired file extension (e.g., '.jpg')

selective_copy(source_folder, destination_folder, file_extension)
