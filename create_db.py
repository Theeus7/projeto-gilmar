import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'resumos.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('DROP TABLE IF EXISTS livros')

cursor.execute('''
CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,          -- Nome do PDF (ou do Livro)
    resumo TEXT NOT NULL,          -- O resumo gerado pela IA
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP -- Data de criação automática
)
''')

conn.commit()
conn.close()

print(f"Banco de dados criado com sucesso em: {DB_PATH}")
