from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from app.core.config import settings
from app.core.constants import LLM_MODEL


def get_llm():
    return ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0.2
    )


def generate_answer(query: str, docs):
    llm = get_llm()

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful assistant.
Answer ONLY using the provided context.

Context:
{context}

Question:
{query}

If the answer is not in the context, say:
"I don't have enough information based on the provided documents."
"""

    messages = [
        SystemMessage(content="You are a precise RAG assistant."),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)

    return response.content