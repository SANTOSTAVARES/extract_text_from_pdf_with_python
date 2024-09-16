from PyPDF2 import PdfReader


with open("ConexaoAgro.pdf", "rb") as input_pdf:

    pdf_reader = PdfReader(input_pdf)
    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        print("Texto da página", page_number + 1, ":", text)
