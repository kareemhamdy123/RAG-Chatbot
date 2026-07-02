from fastapi import APIRouter

from app.models.schemas import (
    ChatRequest
)

from app.memory.chat_memory import (
    get_history,
    add_user_message,
    add_ai_message,
    clear_history
)

from app.services.rag_service import (
    rag_service
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Horizon RAG API Running"
    }


@router.post("/chat")
def chat(request: ChatRequest):

    history = get_history(
        request.session_id
    )

    result = rag_service.ask(
        request.question,
        history
    )

    add_user_message(
        request.session_id,
        request.question
    )

    add_ai_message(
        request.session_id,
        result["answer"]
    )

    return {
        "session_id": request.session_id,
        "answer": result["answer"],
        "sources": result["sources"]
    }


@router.delete("/chat/{session_id}")
def delete_chat(session_id: str):

    clear_history(session_id)

    return {
        "message": "Conversation cleared"
    }