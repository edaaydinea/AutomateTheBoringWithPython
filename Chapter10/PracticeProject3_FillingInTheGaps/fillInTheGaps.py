import os
import re

def fill_gaps(folder, prefix):
    # Regex to match the given prefix followed by numbers (e.g., spam001.txt)
    pattern = re.compile(r'^(' + re.escape(prefix) + r')(\d+)(\..+)$')
    
    # Create a list of files with the given prefix
    files = []
    for filename in os.listdir(folder):
        match = pattern.match(filename)
        if match:
            files.append(filename)
    
    # Sort the files by the number in their filename
    files.sort(key=lambda x: int(pattern.match(x).group(2)))
    
    # Rename files to close gaps in numbering
    expected_number = 1
    for filename in files:
        match = pattern.match(filename)
        current_number = int(match.group(2))
        extension = match.group(3)
        
        if current_number != expected_number:
            # Rename the file to close the gap
            new_filename = f'{prefix}{expected_number:03}{extension}'
            print(f'Renaming {filename} to {new_filename}')
            old_file_path = os.path.join(folder, filename)
            new_file_path = os.path.join(folder, new_filename)
            os.rename(old_file_path, new_file_path)
        
        expected_number += 1

# Example usage
folder = './Chapter10/PracticeProject3_FillingInTheGaps'  # Replace with your folder path
prefix = 'spam'  # Replace with the prefix of your files

fill_gaps(folder, prefix)
