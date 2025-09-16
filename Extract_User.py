import PyPDF2
import docx


class TextExtractor:
    def __init__(self, path):
        self.path = path
        self.format = self.predict_format(path)
        self.text = ""
        if self.format == 1:
            self.text = self.extract_text_from_pdf()
        elif self.format == 0:
            self.text = self.extract_text_from_docx()
        else:
            with open(path, "r") as file:
                text = file.read()
            self.text = text

    def predict_format(self, path):
        if path.endswith(".pdf"):
            return 1
        elif path.endswith(".docx"):
            return 0

    def extract_text_from_pdf(self):
        text = ""
        with open(self.path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text

    def extract_text_from_docx(self):

        document = docx.Document(self.path)
        text = ""
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
        return text
