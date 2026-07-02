import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Horizon AI Assistant",
    page_icon="✈️",
    layout="wide"
)

st.title(
    "✈️ Horizon Tours & Travel Assistant"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.write(
            msg["content"]
        )

prompt = st.chat_input(
    "Ask a question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    try:

        response = requests.post(
            API_URL,
            json={
                "session_id": "kareem",
                "question": prompt
            },
            timeout=60
        )

        answer = response.json()["answer"]

    except Exception as e:

        answer = f"Error: {str(e)}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message(
        "assistant"
    ):
        st.write(answer)