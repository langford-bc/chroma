#from helper_utils import word_wrap # helper functions from utilities
from pypdf import PdfReader

reader = PdfReader("/Users/deen/Documents/chromadb-test/tut-chroma-clearai/microsoft_annual_report_2022.pdf")
pdf_texts = [p.extract_text().strip() for p in reader.pages]

# Filter the empty strings
pdf_texts = [text for text in pdf_texts if text]

print(pdf_texts[0])




