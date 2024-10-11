#! python3
# extractPages.py - Extracts specific pages from a PDF and saves them as a new PDF.

import PyPDF2
import os

def extract_pages(input_pdf, output_pdf, page_numbers):
    pdfReader = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through the page numbers and add them to the new PDF
    for pageNum in page_numbers:
        if pageNum < pdfReader.numPages:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    # Save the extracted pages to a new PDF
    with open(output_pdf, 'wb') as pdfOutput:
        pdfWriter.write(pdfOutput)

# Example usage:
input_pdf = './Chapter15/Project1/allminutes.pdf'
output_pdf = './Chapter15/Project1/extracted_pages.pdf'
pages_to_extract = [0, 2, 4]  # Extract pages 1, 3, 5 (0-based index)

extract_pages(input_pdf, output_pdf, pages_to_extract)
