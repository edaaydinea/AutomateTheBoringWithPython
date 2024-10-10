import openpyxl
import sys

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Get a list of text files from the command-line arguments
text_files = sys.argv[1:]  # Assuming you pass filenames as command-line arguments

# Iterate over each file and add its contents to a new column in the spreadsheet
for col_num, text_file in enumerate(text_files, 1):
    with open(text_file, 'r') as file:
        lines = file.readlines()
        
        # Write each line into the corresponding row in the current column
        for row_num, line in enumerate(lines, 1):
            sheet.cell(row=row_num, column=col_num).value = line.strip()  # strip() removes any trailing newline characters

# Save the spreadsheet to a file
wb.save('output_spreadsheet.xlsx')
print(f"Saved the text files into 'output_spreadsheet.xlsx'")
