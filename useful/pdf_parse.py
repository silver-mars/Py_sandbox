from PyPDF2 import PdfFileReader

pdf_document = 'ae_2022-1.pdf'
with open(pdf_document, "rb") as file_handle:
    pdf = PdfFileReader(file_handle)
    info = pdf.getDocumentInfo()
    print("This is info\n")
    print(info)
    pages = pdf.getNumPages()
    print("This is number of pages:\n")
    print(f"number of pages: {pages}")
    page1 = pdf.getPage(0)
    print("This is page #1\n")
    print(page1)
    print("This is extractText() page #1\n")
    print(page1.extractText(), '\n')
    page2 = pdf.getPage(1)
    print(page2.extractText())
