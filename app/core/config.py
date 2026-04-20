from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or GEMINI_API_KEY
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", str(BASE_DIR / "db"))
    SOURCE_DOCS_PATH = os.getenv("SOURCE_DOCS_PATH", str(BASE_DIR / "data" / "source_docs"))

settings = Settings()