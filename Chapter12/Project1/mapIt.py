# Step 1: Figure Out the URL Parameters
# Step 2: Handle the Command Line Arguments

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)