# 📄 Leucine Backend Assignment

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) based backend application built using FastAPI. It allows users to upload PDF documents, stores and searches document content using vector embeddings (FAISS), and answers user questions using Google's Gemini AI model.

---

## Features

- User Signup and Login (JWT Authentication)
- Secure Password Hashing
- PostgreSQL Database Integration
- Upload PDF Documents
- Extract Text from PDFs
- Split Text into Chunks
- Generate Sentence Embeddings
- Store Embeddings using FAISS
- Semantic Search on Uploaded Documents
- AI-powered Question Answering using Gemini
- Interactive API Documentation with Swagger UI

---

## Tech Stack

### Backend
- FastAPI
- Python

### Database
- PostgreSQL
- SQLAlchemy

### Authentication
- JWT (JSON Web Token)
- Passlib (Password Hashing)

### AI / RAG
- Google Gemini API
- Sentence Transformers
- FAISS

### PDF Processing
- PyMuPDF (fitz)

### Others
- Uvicorn
- Pydantic
- Python-dotenv

---

## Project Structure

```text
leucine_assignment/

app/
│── routers/
│     ├── auth_router.py
│     ├── document_router.py
│     └── chat_router.py
│
│── auth.py
│── database.py
│── main.py
│── middleware.py
│── models.py
│── rag.py
│── schemas.py
│── utils.py

uploads/

.env
requirements.txt
README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd leucine_assignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/leucine_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

GEMINI_API_KEY=your_gemini_api_key
```

---

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

Server URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /auth/signup | Register a new user |
| POST | /auth/login | Login and receive JWT token |

---

### Documents

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /documents/upload | Upload PDF document |

---

### Chat

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chat | Ask questions about uploaded documents |

---

## Workflow

1. Register a new user.
2. Login and obtain a JWT token.
3. Upload a PDF document.
4. The PDF text is extracted and split into chunks.
5. Embeddings are generated using Sentence Transformers.
6. Embeddings are stored in a FAISS vector index.
7. User asks a question.
8. Relevant document chunks are retrieved.
9. Gemini generates an answer based on the retrieved context.

---

## Future Improvements

- Store FAISS embeddings permanently.
- Support multiple PDF uploads.
- Add document management (view/delete).
- Improve prompt engineering.
- Add chat history.
- Docker deployment.

---

## Author

**Sridevi**

Computer Science Engineering Student

Python | FastAPI | PostgreSQL | AI | RAG