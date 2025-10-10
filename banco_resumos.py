import sqlite3

# Nome do banco
conn = sqlite3.connect('resumos.db')
cursor = conn.cursor()

# Habilita chaves estrangeiras (boa prática, mesmo com 1 tabela)
cursor.execute('PRAGMA foreign_keys = ON;')

# Remove tabela se já existir (útil ao testar)
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

# Dados de exemplo (opcional)
cursor.execute('''
INSERT INTO livros (autor, editora, titulo, arquivo_pdf, resumo)
VALUES (?, ?, ?, ?, ?)
''', (
    "Machado de Assis",
    "Editora Garnier",
    "Dom Casmurro",
    "uploads/dom_casmurro.pdf",
    "Romance clássico que aborda ciúme, memória e ambiguidade narrativa."
))

conn.commit()
conn.close()
print("✅ Banco de dados criado com sucesso: resumos.db")
