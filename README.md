# ![Logo do Projeto](static/images/logo-light.png)

# Titulo
- SRLP – Sistema de Resumos de Livros em PDF


## 🎯 Objetivos

- Desenvolver uma aplicação capaz de armazenar livros em PDF, aplicar técnicas de Inteligência Artificial para gerar resumos automáticos e organizados, permitir a pesquisa por título, autor ou gênero, oferecer leitura e download dos resumos, e disponibilizar um painel simples para gerenciamento dos arquivos.

---

## 🧠 Inteligência Artificial 
- Utiliza algoritmos de Processamento de Linguagem Natural (PLN) para compreender o conteúdo dos livros.

- Identifica automaticamente as partes mais relevantes de cada texto.

- Gera resumos coerentes e objetivos, mantendo o sentido original do livro.

- Pode ser treinada com novos textos para melhorar a qualidade dos resumos.

---


## 🚀 Funcionalidades

- Cadastro e listagem de livros e resumos.  
- Armazenamento local com **SQLite**.  
- Interface simples feita com HTML, CSS e JavaScript.  
- API REST criada com Flask e organizada por Blueprints.  

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **Flask-CORS**
- **SQLite3**
- **HTML / CSS / JS**

---

## ✅ Rodando Localmente

Siga os passos abaixo para executar o projeto em sua máquina local:

---

### 1 Clonar o repositório:
```bash
git clone https://github.com/Matheus686/PROJETO-GILMAR.git
cd PROJETO-GILMAR

### 2 Criar e ativar o ambiente virtual:

-(Windows) 
python -m venv venv
venv\Scripts\activate

-(Linux/Mac) 
python3 -m venv venv
source venv/bin/activate

### 3 CInstalar as dependências:

- pip install -r requirements.txt

### 4 Criar o banco de dados:

- python create_db.py

### 5 Executar a aplicação Flask:

- python app.py

### 6 Acessar no navegador:

- http://127.0.0.1:5000


  
## 📁 Estrutura do Projeto

```
PROJETO-GILMAR/
│
├── app.py                     ← seu arquivo Flask principal
├── config.py                  ← suas configurações Flask (já existe)
├── create_db.py               ← Banco de dados. 
│
│
├── static/                    ← mantém igual
│   ├── images/
│   │   ├── history-dark.png
│   │   ├── history-light.png
│   │   ├── ...
│   ├── main.js
│   └── styles.css
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md

```

---

## 👥 Equipe

| Nome            | GitHub                                           |
|-----------------|--------------------------------------------------|
| Luis Hardt      | [@Luis](https://github.com/Luis-Hardt)           |
| Marcos Antônio  | [@Marcos](https://github.com/MacQueenDev)        |
| Matheus Ortela  | [@MatheusOrtela](https://github.com/Theeus7)     |                  |
| Matheus Soares  | [@MatheusSoares](https://github.com/Matheus686)  |
| Thales Eduardo  | [@Thales](https://github.com/Fridayzin)          |

---

## 🏫 Informações Acadêmicas

- **Universidade:** Universidade Braz Cubas  
- **Curso:** Ciência da Computação  
- **Semestre:** 3º e 4º
- **Período:** Noite  
- **Professora orientador:** Gilmar Alexandre Do Prado Yahuita  

---

## 📄 Licença

Este projeto foi desenvolvido com propósito **acadêmico** e **educacional**, integrando a avaliação da disciplina.

---



