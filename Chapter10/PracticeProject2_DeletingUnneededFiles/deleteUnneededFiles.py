import os

def find_large_files(folder, size_limit_mb):
    size_limit_bytes = size_limit_mb * 1024 * 1024  # Convert MB to bytes

    # Walk through the folder tree
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Get the full path of the file
            file_path = os.path.join(foldername, filename)
            try:
                # Get the size of the file
                file_size = os.path.getsize(file_path)
                # Check if the file size exceeds the limit
                if file_size > size_limit_bytes:
                    # Convert file size to MB for display
                    file_size_mb = file_size / (1024 * 1024)
                    print(f'{file_path} - {file_size_mb:.2f} MB')
                else:
                    print(f'{file_path} - {file_size} bytes')
            except FileNotFoundError:
                # If a file is not found (e.g., if it was deleted after starting the search), skip it
                print(f"File not found: {file_path}")
            except PermissionError:
                # Skip files that cannot be accessed due to permission issues
                print(f"Permission denied: {file_path}")

# Example usage
folder_to_search = "./Chapter10/PracticeProject2_DeletingUnneededFiles"  # Replace with your folder path
size_limit_mb = 100  # Replace with your size limit in MB

find_large_files(folder_to_search, size_limit_mb)
