import PyPDF2
from typing import Optional

class PDFService:
    @staticmethod
    def extract_text(file_path: str) -> Optional[str]:
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text.strip()
        except Exception as e:
            raise Exception(f"Erro ao extrair texto do PDF: {str(e)}")
    
    @staticmethod
    def validate_pdf(file) -> bool:
        return file and file.filename.lower().endswith('.pdf')