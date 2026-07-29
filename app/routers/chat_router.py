from fastapi import APIRouter
from google import genai
from dotenv import load_dotenv
import os

from app.schemas import ChatRequest
from app.rag import search_documents

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(request: ChatRequest):
    try:

        context = search_documents(request.question)

        if context == "":
            context = "No document uploaded."

        prompt = f"""
You are a helpful AI assistant.

Context:
{context}

Question:
{request.question}

Answer based only on the context if possible.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "answer": response.text
        }

    except Exception as e:
        print(e)

        return {
            "error": str(e)
        }