import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from services.pdf_service import PDFService
from services.openai_service import GeminiService
from config import Config

book_bp = Blueprint('books', __name__)
pdf_service = PDFService()

@book_bp.route('/upload', methods=['POST'])
def upload_book():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    if not pdf_service.validate_pdf(file):
        return jsonify({'error': 'Arquivo deve ser um PDF'}), 400
    
    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        file.save(file_path)
        
        text = pdf_service.extract_text(file_path)
        if not text:
            return jsonify({'error': 'Não foi possível extrair texto do PDF'}), 400
        
        gemini_service = GeminiService()
        summary = gemini_service.generate_summary(text)
        
        os.remove(file_path)  # Remove arquivo após processamento
        
        return jsonify({
            'filename': filename,
            'summary': summary
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@book_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200