from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pathlib import Path

from core.constants import (
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    COLLECTION_NAME,
)
from core.config import settings


def load_documents(docs_path=None):
    resolved_docs_path = Path(docs_path or settings.SOURCE_DOCS_PATH).resolve()
    if not resolved_docs_path.exists():
        raise FileNotFoundError(f"Directory not found: '{resolved_docs_path}'")

    loader = DirectoryLoader(
        path=str(resolved_docs_path),
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    return loader.load()


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)


def create_vector_store(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=settings.CHROMA_DB_PATH,
        collection_name=COLLECTION_NAME,
    )

    return vectorstore


def run_ingestion(docs_path=None):
    source_path = docs_path or settings.SOURCE_DOCS_PATH

    documents = load_documents(source_path)
    if not documents:
        return 0

    chunks = split_documents(documents)
    create_vector_store(chunks)

    return len(chunks)