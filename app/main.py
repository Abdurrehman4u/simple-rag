from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="RAG System",
    description="Simple RAG using Chroma + Gemini + FastAPI",
    version="1.0.0"
)

app.include_router(router)