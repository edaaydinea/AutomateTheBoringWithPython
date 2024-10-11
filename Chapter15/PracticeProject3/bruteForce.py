import PyPDF2
from tqdm import tqdm

def brute_force_pdf_password(pdf_filename, dictionary_filename):
    with open(dictionary_filename, 'r') as dict_file:
        words = dict_file.readlines()
    
    with open(pdf_filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Use tqdm to create a progress bar
        for word in tqdm(words, desc="Trying passwords", unit="word"):
            word = word.strip()
            if reader.decrypt(word.lower()) == 1:
                print(f'\nPassword found: {word.lower()}')
                return
            elif reader.decrypt(word.upper()) == 1:
                print(f'\nPassword found: {word.upper()}')
                return

        print('\nPassword not found.')

# Usage
brute_force_pdf_password('encrypted.pdf', 'dictionary.txt')
