from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from core.constants import (
    EMBEDDING_MODEL,
    TOP_K_RESULTS,
    COLLECTION_NAME
)
from core.config import settings


def load_vector_store():
    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    db = Chroma(
        persist_directory=settings.CHROMA_DB_PATH,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME
    )

    return db


def retrieve_documents(query: str):
    db = load_vector_store()

    retriever = db.as_retriever(
        search_kwargs={"k": TOP_K_RESULTS}
    )

    relevant_docs = retriever.invoke(query)

    return relevant_docs