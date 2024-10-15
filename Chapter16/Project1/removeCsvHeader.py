import csv
import os

# Create a directory to store the CSV files without headers.
os.makedirs('headerRemoved', exist_ok=True)

# Walk through all directories and subdirectories.
for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        # Process only CSV files.
        if not filename.endswith('.csv'):
            continue

        # Full path of the file.
        csvFilePath = os.path.join(foldername, filename)

        print(f'Removing header from {csvFilePath}...')

        # Read the CSV file (skipping the first row).
        csvRows = []
        with open(csvFilePath, 'r', newline='') as csvFileObj:
            readerObj = csv.reader(csvFileObj)
            for row in readerObj:
                if readerObj.line_num == 1:
                    continue  # Skip first row.
                csvRows.append(row)

        # Write the CSV file without the header in the headerRemoved folder.
        # Ensure the folder structure is preserved.
        relativeFolder = os.path.relpath(foldername, '.')
        newFolder = os.path.join('headerRemoved', relativeFolder)
        os.makedirs(newFolder, exist_ok=True)  # Create subdirectories if necessary

        newCsvFilePath = os.path.join(newFolder, filename)
        with open(newCsvFilePath, 'w', newline='') as csvFileObj:
            csvWriter = csv.writer(csvFileObj)
            for row in csvRows:
                csvWriter.writerow(row)

print('Header removal complete.')
