from pypdf import PdfReader

def read_pdf(path):
    text = ""
    reader = PdfReader(path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text