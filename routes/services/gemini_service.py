import google.generativeai as genai
from config import Config

class GeminiService:
    def __init__(self):
        if not Config.GOOGLE_API_KEY:
            raise Exception("Chave da API não configurada. Defina GOOGLE_API_KEY no arquivo .env.")
        
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def generate_summary(self, text: str) -> str:
        try:
            prompt = f"""
Você é um assistente literário especializado em análises e resumos de livros completos.
Leia atentamente o texto enviado e produza um resumo claro, coeso e informativo do conteúdo integral da obra — 
não apenas da sinopse.

O resumo deve abordar:
- Enredo principal e sua progressão;
- Personagens centrais e seus papéis na história;
- Contexto e temas abordados (sociais, psicológicos, filosóficos, etc.);
- Desfecho e mensagem principal do livro.

Evite repetir trechos introdutórios, sinopses ou comentários externos. 
Escreva de forma objetiva, sem adicionar opiniões pessoais e sem usar caracteres especiais.

A:\n\n{text}
"""
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Erro ao gerar resumo: {str(e)}")
