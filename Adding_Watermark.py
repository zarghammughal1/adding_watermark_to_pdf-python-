"""
  The code will add the watermark into the pdf file.
  Get the pdf file, watermark, and then add waterark to the pages of pdf file.
"""
import PyPDF2
pdf_file = "doc.pdf"
watermark = "watermark.pdf"
merged_file = "merged.pdf"
input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)
watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
pdf_page = input_pdf.getPage(0)
watermark_page = watermark_pdf.getPage(0)
pdf_page.mergePage(watermark_page)
output = PyPDF2.PdfFileWriter()
output.addPage(pdf_page)
merged_file = open(merged_file,'wb')
output.write(merged_file)
merged_file.close()
watermark_file.close()
input_file.close()
