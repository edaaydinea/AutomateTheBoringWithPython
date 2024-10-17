import os
from PIL import Image

# Define what qualifies as a photo
MIN_PHOTO_SIZE = 500  # pixels
PHOTO_EXTENSIONS = ('.png', '.jpg', '.jpeg')

# Walk through all directories
for foldername, subfolders, filenames in os.walk('C:\\'):  # Adjust the path as needed
    numPhotoFiles = 0
    numNonPhotoFiles = 0

    for filename in filenames:
        # Check file extension
        if not filename.lower().endswith(PHOTO_EXTENSIONS):
            numNonPhotoFiles += 1
            continue

        # Open image file to check size
        try:
            with Image.open(os.path.join(foldername, filename)) as img:
                width, height = img.size
                if width > MIN_PHOTO_SIZE and height > MIN_PHOTO_SIZE:
                    numPhotoFiles += 1
                else:
                    numNonPhotoFiles += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            numNonPhotoFiles += 1

    # Check if more than half are photo files
    if numPhotoFiles > (numPhotoFiles + numNonPhotoFiles) / 2:
        print(f"Photo folder found: {os.path.abspath(foldername)}")
