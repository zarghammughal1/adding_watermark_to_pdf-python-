
'''
#Add Watermark to PDF (Python)
#Import Files
just add watermark and pdf file

'''
import PyPDF2
import sys

#Import Files
original = PyPDF2.PdfFileReader(sys.argv[1])
watermark = PyPDF2.PdfFileReader(sys.argv[2])
# Output File
output = PyPDF2.PdfFileWriter()

#Loop until the last page
for i in range(original.getNumPages()):
    page = original.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('Watermarked_PDF.pdf', 'wb') as file:
    output.write(file)
