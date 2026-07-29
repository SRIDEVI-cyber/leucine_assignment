from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app import models

from app.routers import auth_router
from app.routers import document_router
from app.routers import chat_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(title="Leucine RAG Backend")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router.router)
app.include_router(document_router.router)
app.include_router(chat_router.router)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }