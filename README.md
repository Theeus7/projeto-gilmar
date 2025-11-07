# ![Logo do Projeto](static/images/logo-light.png)

# SRLP – Sistema de Resumos de Livros em PDF

## 🎯 Objetivos

Desenvolver uma aplicação capaz de armazenar livros em PDF, aplicar técnicas de Inteligência Artificial para gerar resumos automáticos e organizados, permitir a pesquisa por título, autor ou gênero, oferecer leitura e download dos resumos, e disponibilizar um painel simples para gerenciamento dos arquivos.

## 🧠 Inteligência Artificial

- Utiliza algoritmos de Processamento de Linguagem Natural (PLN) para compreender o conteúdo dos livros
- Identifica automaticamente as partes mais relevantes de cada texto
- Gera resumos coerentes e objetivos, mantendo o sentido original do livro
- Integração com Google Gemini AI para processamento avançado de texto

## 🚀 Funcionalidades

- Upload e processamento de livros em PDF
- Geração automática de resumos usando IA
- Histórico de livros processados
- Interface responsiva com tema claro/escuro
- API REST organizada com Flask Blueprints
- Armazenamento local com SQLite

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Flask** - Framework web
- **Flask-CORS** - Controle de CORS
- **SQLite3** - Banco de dados
- **PyPDF2** - Processamento de PDFs
- **Google Generative AI** - IA para geração de resumos
- **HTML / CSS / JavaScript** - Frontend
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

## ✅ Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/Matheus686/PROJETO-GILMAR.git
cd PROJETO-GILMAR
```

### 2. Criar e ativar ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
GEMINI_API_KEY=sua_chave_api_aqui
```

### 5. Criar banco de dados
```bash
python create_db.py
```

### 6. Executar aplicação
```bash
python app.py
```

### 7. Acessar no navegador
```
http://127.0.0.1:5000
```

## 📁 Estrutura do Projeto

```
PROJETO-GILMAR/
│
├── routes/
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini_service.py
│   │   └── pdf_service.py
│   ├── __init__.py
│   └── book_routes.py
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   ├── logo-light.png
│   │   ├── logo-dark.png
│   │   └── ...
│   ├── js/
│   │   ├── main.js
│   │   ├── history.js
│   │   ├── sidebar.js
│   │   └── themes.js
│   ├── main.js
│   └── styles.css
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── uploads/
├── .env
├── .gitignore
├── app.py
├── config.py
├── create_db.py
├── requirements.txt
├── resumos.db
└── README.md
```

## 📚 API Endpoints

### Livros
- `POST /api/books/upload` - Upload de PDF e geração de resumo
- `GET /api/books/history` - Listar histórico de livros
- `GET /api/books/summary/<id>` - Obter resumo específico

## 👥 Equipe

| Nome            | GitHub                                           |
|-----------------|--------------------------------------------------|
| Luis Hardt      | [@Luis-Hardt](https://github.com/Luis-Hardt)    |
| Marcos Antônio  | [@MacQueenDev](https://github.com/MacQueenDev)   |
| Matheus Ortela  | [@Theeus7](https://github.com/Theeus7)          |
| Matheus Soares  | [@Matheus686](https://github.com/Matheus686)    |
| Thales Eduardo  | [@Fridayzin](https://github.com/Fridayzin)      |

---

## 🏫 Informações Acadêmicas

- **Universidade:** Universidade Braz Cubas  
- **Curso:** Ciência da Computação  
- **Semestre:** 3º e 4º
- **Período:** Noite  
- **Professor Orientador:** Gilmar Alexandre Do Prado Yahuita  

---

## 📄 Licença

Este projeto foi desenvolvido com propósito **acadêmico** e **educacional**, integrando a avaliação da disciplina.

---



