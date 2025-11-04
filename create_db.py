import sqlite3
import os

# Caminho absoluto do banco (fica na raiz do projeto)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'resumos.db')

# Conexão com o banco
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Habilita chaves estrangeiras (boa prática)
cursor.execute('PRAGMA foreign_keys = ON;')

# Remove tabela se já existir (útil durante testes)
cursor.execute('DROP TABLE IF EXISTS livros')

# Cria a tabela principal
cursor.execute('''
CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor TEXT NOT NULL,
    editora TEXT,
    titulo TEXT NOT NULL,
    arquivo_pdf TEXT,          -- caminho/URL do arquivo PDF
    resumo TEXT NOT NULL,
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Confirma e fecha a conexão
conn.commit()
conn.close()

print(f"✅ Banco de dados criado com sucesso em: {DB_PATH}")
