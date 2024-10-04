import zipfile
import os

def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)  # make sure folder is absolute
    
    # Figure out the filename based on existing files.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        # Save ZIP to the current directory (os.getcwd()) or specify another path.
        zip_filepath = os.path.join(os.getcwd(), zip_filename)
        if not os.path.exists(zip_filepath):
            break
        number += 1
    
    # Create the ZIP file in write mode with compression.
    print(f'Creating {zip_filename}...')
    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # Walk the folder tree and compress files.
        for foldername, subfolders, filenames in os.walk(folder):
            print(f"Adding files in {foldername}...")
            # Add the current folder to the ZIP file.
            backup_zip.write(foldername, os.path.relpath(foldername, folder))
            
            # Add files in this folder to the ZIP.
            for filename in filenames:
                new_base = os.path.basename(folder) + '_'
                if filename.startswith(new_base) and filename.endswith('.zip'):
                    continue  # Skip ZIP files created by the script.
                
                # Add files relative to the root folder.
                file_path = os.path.join(foldername, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, folder))
    
    print('Done.')
    
backup_to_zip('./Chapter10/Project2_BackingUpToZip/delicious')
