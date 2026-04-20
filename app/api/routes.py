from fastapi import APIRouter

from app.schemas.query import QueryRequest, QueryResponse
from app.services.ingestions import run_ingestion
from app.services.retreival import retrieve_documents
from app.services.llm import generate_answer

router = APIRouter()

@router.post("/ingest")
def ingest_documents():
    run_ingestion()
    return {"message": "Ingestion completed"}


@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):

    docs = retrieve_documents(request.query)
    answer = generate_answer(request.query, docs)

    return QueryResponse(
        query=request.query,
        answer=answer,
        context_used=len(docs)
    )