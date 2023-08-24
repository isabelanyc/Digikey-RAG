import os
import tabula.io as tabula
from pdfminer.high_level import extract_text
import json
from PyPDF2 import PdfReader

def is_valid_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            if len(reader.pages) > 0:
                return True
        return False
    except Exception as e:
        print(f"An error occurred while processing {pdf_path}: {e}")
        return False

def process_pdf(pdf_path):
    # Extract text content
    text_content = extract_text(pdf_path)

    # Extract tables
    try:
        tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    except json.decoder.JSONDecodeError:
        print(f"Error processing {pdf_path}")
        tables = []

    table_content = "\n".join([table.to_string() for table in tables])

    return text_content + "\n" + table_content

def save_to_txt(content, txt_path):
    with open(txt_path, "w") as file:
        file.write(content)

pdf_data_directory = "data/pdf"
txt_data_directory = "data/txt"

for filename in os.listdir(pdf_data_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_data_directory, filename)
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(txt_data_directory, txt_filename)
        

        if is_valid_pdf(pdf_path=pdf_path):
            content = process_pdf(pdf_path)
            save_to_txt(content, txt_path)
            print(f"Processed {pdf_path} and saved to {txt_path}")
