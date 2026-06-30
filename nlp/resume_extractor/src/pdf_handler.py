import fitz  # from PyMuPDF
def extract_text_from_pdf(pdf_path):
    """Extract text from PDF resume"""
    doc = fitz.open(pdf_path) #open file

    #extract text from pdf line by line 
    text = ""
    for page in doc:
        text = text + page.get_text("text")
    doc.close()
    return text