import os
import pymupdf

from modules.pdf_handler import PDFHandler as pdf

def open_file(root, file_name):
    document = pdf(root,file_name)
    opened_file = pdf.read_file(document)

    print(opened_file)
    return opened_file, document

def extract_file_text(opened_file):
    for page in opened_file: # iterate the document pages
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        return text
    
def transform_matrix(document):

    roi = document[0].transformation_matrix

    return pymupdf.Rect(0, 0, 100, 100) * ~roi

def get_client_name(document):

    text = document[0].get_textbox([300, 70, 550, 150])

    return text

# file, document = open_file("test_files","Facture_20250202-1208-4.pdf")

# test = transform_matrix(file)

# client = get_client(file)

def iterate_repository(repo_path):
    """
    Recursively iterates through a repository and prints all files and directories.
    :param repo_path: Path to the repository
    """
    for root, dirs, files in os.walk(repo_path):
        if 'ZZZZZZZ' in root:
            continue
        print(f"Directory: {root}")
        for file in files:
            if 'Facture' in file:
                # print(f"  File: {os.path.join(root, file)}")
                file, document = open_file(root,file)
                client = get_client_name(file)
                print(client)

# Example usage
repo_path = "/mnt/c/Users/victo/Desktop/Bureau de tabac"  # Change this to your repository path
iterate_repository(repo_path)
