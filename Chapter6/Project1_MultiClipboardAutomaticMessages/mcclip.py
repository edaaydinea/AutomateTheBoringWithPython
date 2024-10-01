#! python3
# mcclip.py - A multi-clipboard program.

# Step 1: Program Design and Data Structures

TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

# Step 2: Handle Command Line Arguments

import sys
if len(sys.argv) < 2:
    print('Usage: python mcclip.py [keyphrase] - copy phrase text')
    sys.exit()
    
keyphrase = sys.argv[1] # first command line arg is the keyphrase

# Step 3: Copy the Right Phrase

import pyperclip

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}.')