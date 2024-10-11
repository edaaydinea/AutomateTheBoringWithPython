#! python3
# reorderPages.py - Reorders pages in a PDF and saves the result.

import PyPDF2
import os

def reorder_pages(input_pdf, output_pdf, new_order):
    pdfReader = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through the new order and add pages accordingly
    for pageNum in new_order:
        if pageNum < pdfReader.numPages:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    # Save the reordered pages to a new PDF
    with open(output_pdf, 'wb') as pdfOutput:
        pdfWriter.write(pdfOutput)

# Example usage:
input_pdf = './Chapter15/Project1/allminutes.pdf'
output_pdf = './Chapter15/Project1/reordered_pages.pdf'
new_page_order = [2, 0, 1]  # Reorder to: page 3, page 1, page 2

reorder_pages(input_pdf, output_pdf, new_page_order)
