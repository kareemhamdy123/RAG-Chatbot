conversations = {}


def get_history(session_id: str):
    return conversations.setdefault(session_id, [])


def add_user_message(session_id: str, message: str):
    conversations.setdefault(session_id, [])
    conversations[session_id].append(
        f"Human: {message}"
    )


def add_ai_message(session_id: str, message: str):
    conversations.setdefault(session_id, [])
    conversations[session_id].append(
        f"AI: {message}"
    )


def clear_history(session_id: str):
    conversations.pop(session_id, None)