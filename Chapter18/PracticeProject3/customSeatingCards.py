from PIL import Image, ImageDraw, ImageFont
import os

# Constants
CARD_WIDTH, CARD_HEIGHT = 288, 360
GUESTS_FILE = 'guests.txt'
FLOWER_IMAGE = 'flower.png'  # Replace with path to flower image
OUTPUT_FOLDER = 'seating_cards'

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load the flower decoration and ensure it has an alpha channel
flower = Image.open(FLOWER_IMAGE).convert('RGBA').resize((100, 100))  # Adjust size as needed

# Prepare font
try:
    font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()

# Read guests from file
with open(GUESTS_FILE, 'r') as file:
    guests = [line.strip() for line in file.readlines()]

# Generate seating cards
for guest in guests:
    # Create a blank card
    card = Image.new('RGBA', (CARD_WIDTH, CARD_HEIGHT), 'white')
    draw = ImageDraw.Draw(card)

    # Paste the flower decoration (optional)
    card.paste(flower, (10, 10), mask=flower)

    # Draw the guest's name
    bbox = draw.textbbox((0, 0), guest, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (CARD_WIDTH - text_width) // 2
    y = (CARD_HEIGHT - text_height) // 2
    draw.text((x, y), guest, fill='black', font=font)

    # Draw cutting guideline
    draw.rectangle([(5, 5), (CARD_WIDTH - 5, CARD_HEIGHT - 5)], outline='black', width=3)

    # Save the card
    card.save(os.path.join(OUTPUT_FOLDER, f'{guest}_card.png'))
    print(f"Created card for {guest}")
