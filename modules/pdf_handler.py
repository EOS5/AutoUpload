import pymupdf as pdf

class PDFHandler:

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def get_file_name(self):
        return self.file_name
    
    def get_file_path(self):
        return self.file_path

    def read_file(self):
        doc = pdf.open(f"{self.file_path}/{self.file_name}")
        return doc
