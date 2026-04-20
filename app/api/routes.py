from fastapi import APIRouter, HTTPException

from schemas.query import QueryRequest, QueryResponse
from services.ingestions import run_ingestion
from services.retreival import retrieve_documents
from services.llm import generate_answer

router = APIRouter()

@router.post("/ingest")
def ingest_documents():
    run_ingestion()
    return {"message": "Ingestion completed"}


@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):

    docs = retrieve_documents(request.query)
    try:
        answer = generate_answer(request.query, docs)
    except ValueError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return QueryResponse(
        query=request.query,
        answer=answer,
        context_used=len(docs)
    )