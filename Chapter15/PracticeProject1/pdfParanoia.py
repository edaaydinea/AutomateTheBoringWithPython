import os
import sys
import PyPDF2

def encrypt_pdfs(folder, password):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'rb') as pdf_file:
                    reader = PyPDF2.PdfFileReader(pdf_file)
                    writer = PyPDF2.PdfFileWriter()

                    for page_num in range(reader.numPages):
                        writer.addPage(reader.getPage(page_num))
                    
                    writer.encrypt(password)

                    encrypted_filename = filename.replace('.pdf', '_encrypted.pdf')
                    print(f'Encrypting {filename}...')
                    encrypted_filepath = os.path.join(foldername, encrypted_filename)
                    with open(encrypted_filepath, 'wb') as encrypted_pdf_file:
                        writer.write(encrypted_pdf_file)
                
                # Verify encryption
                with open(encrypted_filepath, 'rb') as pdf_file:
                    reader = PyPDF2.PdfFileReader(pdf_file)
                    if reader.isEncrypted:
                        reader.decrypt(password)
                        try:
                            reader.getPage(0)  # Try accessing a page
                            os.remove(filepath)  # Delete original if decryption succeeds
                        except Exception as e:
                            print(f'Error verifying {filename}: {e}')

def decrypt_pdfs(folder, password):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if '_encrypted.pdf' in filename:
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'rb') as pdf_file:
                    reader = PyPDF2.PdfFileReader(pdf_file)
                    
                    if reader.isEncrypted:
                        if reader.decrypt(password) == 1:
                            writer = PyPDF2.PdfFileWriter()
                            for page_num in range(reader.numPages):
                                writer.addPage(reader.getPage(page_num))
                            
                            decrypted_filename = filename.replace('_encrypted', '_decrypted')
                            decrypted_filepath = os.path.join(foldername, decrypted_filename)
                            with open(decrypted_filepath, 'wb') as decrypted_pdf_file:
                                writer.write(decrypted_pdf_file)
                        else:
                            print(f'Incorrect password for {filename}')

def main():
    if len(sys.argv) != 4:
        print('Usage: python pdfParanoia.py [encrypt|decrypt] folder password')
        sys.exit(1)
    
    action = sys.argv[1]
    folder = sys.argv[2]
    password = sys.argv[3]

    if action == 'encrypt':
        encrypt_pdfs(folder, password)
        print('Encryption complete.')
    elif action == 'decrypt':
        decrypt_pdfs(folder, password)
        print('Decryption complete.')
    else:
        print('Invalid action. Use "encrypt" or "decrypt".')
        

if __name__ == '__main__':
    main()