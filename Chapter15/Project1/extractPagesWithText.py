#! python3
# extractPagesWithText.py - Extracts pages that contain a specific text from a PDF.

import PyPDF2
from PyPDF2.pdf import PageObject
import os

def extract_pages_with_text(input_pdf, output_pdf, search_text):
    pdfReader = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through the pages and search for the text
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText()

        if search_text.lower() in text.lower():
            pdfWriter.addPage(pageObj)

    # Save the pages that contain the text
    with open(output_pdf, 'wb') as pdfOutput:
        pdfWriter.write(pdfOutput)

# Example usage:
input_pdf = './Chapter15/Project1/allminutes.pdf'
output_pdf = './Chapter15/Project1/pages_with_text.pdf'
search_text = "LSMSA"

extract_pages_with_text(input_pdf, output_pdf, search_text)
