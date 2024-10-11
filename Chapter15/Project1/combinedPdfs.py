#! python3
# combinedPdfs.py - Combines all the PDFs in the current working directory into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []

folder = "./Chapter15"

for filename in os.listdir(folder):
    if filename.endswith('.pdf'):
        pdfFiles.append(os.path.join(folder, filename))
        
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    # if the file is not decrypt
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # Check if the file is encrypted
    if not pdfReader.isEncrypted:
        # Loop through all the pages (except the first) and add them.
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
# Save the resulting PDF to a file.
save_folder = os.path.join(folder, 'Project1')

pdfOutput = open(os.path.join(save_folder, 'allminutes.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
