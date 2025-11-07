import google.generativeai as genai
from config import Config

class GeminiService:
    def __init__(self):
<<<<<<< HEAD
        if not Config.GOOGLE_API_KEY:
            raise Exception("Chave da API não configurada. Defina GOOGLE_API_KEY no arquivo .env.")
        
        genai.configure(api_key=Config.GOOGLE_API_KEY)
=======
        genai.configure(api_key=Config.GEMINI_API_KEY)
>>>>>>> 0eade81c7ef95c78542c132cb905eb3790e63584
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def generate_summary(self, text: str) -> str:
        try:
            prompt = f"Você é um assistente especializado em criar resumos concisos e informativos de livros. Faça um resumo detalhado do seguinte texto de livro:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Erro ao gerar resumo: {str(e)}")