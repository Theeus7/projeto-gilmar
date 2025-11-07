import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(os.path.dirname(BASE_DIR), '.env') if not os.path.exists(os.path.join(BASE_DIR, '.env')) else os.path.join(BASE_DIR, '.env')

load_dotenv()

class Config:
    GOOGLE_API_KEY  = os.getenv('GOOGLE_API_KEY')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024