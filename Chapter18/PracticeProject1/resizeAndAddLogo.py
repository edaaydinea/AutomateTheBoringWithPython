from PIL import Image
import os

# Constants
LOGO_FILENAME = 'catlogo.png'
OUTPUT_FOLDER = 'output_images'
MAX_SIZE = 300
SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Load the logo image
logo = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo.size

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Loop over all supported files in the working directory
for filename in os.listdir('.'):
    if not filename.lower().endswith(SUPPORTED_FORMATS):
        continue

    if filename == LOGO_FILENAME:
        continue

    # Open the image file
    with Image.open(filename) as img:
        width, height = img.size

        # Check if image is at least twice as large as the logo
        if width < 2 * logo_width or height < 2 * logo_height:
            print(f"Skipping {filename}: Image too small to add the logo.")
            continue

        # Resize the image if necessary
        if width > MAX_SIZE or height > MAX_SIZE:
            if width > height:
                new_width = MAX_SIZE
                new_height = int((MAX_SIZE / width) * height)
            else:
                new_height = MAX_SIZE
                new_width = int((MAX_SIZE / height) * width)

            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Paste the logo into the bottom-right corner
        img.paste(logo, (new_width - logo_width, new_height - logo_height), logo)

        # Save the modified image to the output folder
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        img.save(output_path)
        print(f'Saved modified image: {output_path}')
