from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import auth_router
from app.routers import document_router
from app.routers import chat_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(title="Leucine RAG Backend")

# Register routers
app.include_router(auth_router.router)
app.include_router(document_router.router)
app.include_router(chat_router.router)

@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }