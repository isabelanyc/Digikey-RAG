from langchain.document_loaders import MathpixPDFLoader
import os

folder_path = 'data'
file_paths = []

try:
    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)
        if os.path.isfile(full_path):
            if file_name.endswith('.pdf'):
                file_paths.append(full_path)
            else:
                print(f"{file_name} is not a PDF file.")
except Exception as e:
    print(f"Not a PDF: {e}")

# Load the documents
loaders = []
for path in file_paths:
    loader = MathpixPDFLoader(path)
    loaders.append(loader)


# Transform the documents

# Use Chroma
