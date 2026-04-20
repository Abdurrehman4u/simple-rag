from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    CHROMA_DB_PATH = "db"
    SOURCE_DOCS_PATH = "data/source_docs"

settings = Settings()