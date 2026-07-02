from langchain_openai import ChatOpenAI

from app.core.config import (
    GROQ_API_KEY,
    MODEL_NAME,
    GROQ_BASE_URL
)


def get_llm():
    return ChatOpenAI(
        model=MODEL_NAME,
        openai_api_key=GROQ_API_KEY,
        openai_api_base=GROQ_BASE_URL,
        temperature=0.3
    )