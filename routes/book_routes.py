import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from routes.services.pdf_service import PDFService
from routes.services.gemini_service import GeminiService
from config import Config
import sqlite3
import os

book_bp = Blueprint('books', __name__)
pdf_service = PDFService()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'resumos.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return conn

@book_bp.route('/upload', methods=['POST'])
def upload_book():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    if not pdf_service.validate_pdf(file):
        return jsonify({'error': 'Arquivo deve ser um PDF'}), 400
    
    # Inicializa file_path fora do try para garantir que esteja acessível no except
    file_path = None
    
    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        file.save(file_path)
        
        text = pdf_service.extract_text(file_path)
        if not text:
            # Garante que o arquivo temporário seja removido em caso de falha na extração
            os.remove(file_path)
            return jsonify({'error': 'Não foi possível extrair texto do PDF'}), 400
        
        gemini_service = GeminiService()
        summary = gemini_service.generate_summary(text)
        
        # --- Lógica para salvar no banco de dados (SIMPLIFICADA) ---
        titulo_livro = os.path.splitext(filename)[0] # Usa o nome do arquivo sem a extensão .pdf

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO livros (titulo, resumo)
                VALUES (?, ?)
            """, (titulo_livro, summary))
            conn.commit()
            conn.close()
            
        except Exception as db_e:
            print(f"ERRO AO SALVAR O RESUMO NO DB: {db_e}")
            os.remove(file_path) # Remove o arquivo temporário antes de retornar o erro
            return jsonify({'error': f"Erro ao salvar o resumo no histórico: {str(db_e)}"}), 500

        os.remove(file_path)  # Remove arquivo após processamento
        
        return jsonify({
            'filename': filename,
            'summary': summary
        }), 200
        
    except Exception as e:
        # Garante que o arquivo temporário seja removido em caso de qualquer outra exceção
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({'error': str(e)}), 500

# Função get_db_connection já estava definida acima

@book_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200


@book_bp.route('/history', methods=['GET'])
def get_history():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Selecionando apenas os campos existentes na nova tabela
        cursor.execute("""
            SELECT id, titulo, resumo, criado_em
            FROM livros
            ORDER BY datetime(criado_em) DESC
        """)
        livros = cursor.fetchall()
        conn.close()

        livros_list = [dict(livro) for livro in livros]

        return jsonify({
            "success": True,
            "total": len(livros_list),
            "data": livros_list
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
