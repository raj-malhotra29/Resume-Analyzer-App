import fitz  # Yeh PyMuPDF library hai

def extract_text_from_pdf(pdf_file):
    """
    Function PDF file object leta hai aur uska text return karta hai.
    """
    try:
        # pdf_file ek 'BytesIO' object hota hai jab hum streamlit se upload karte hain
        # isliye hum stream parameter use karte hain
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        
        text = ""
        for page in doc:
            text += page.get_text() # Har page ka text add karein
        
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"