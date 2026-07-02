from langchain_core.prompts import ChatPromptTemplate

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import (
    create_stuff_documents_chain
)

from app.services.llm_service import get_llm
from app.services.vector_store import get_retriever


class RAGService:

    def __init__(self):

        self.retriever = get_retriever()

        self.llm = get_llm()

        prompt = ChatPromptTemplate.from_template(
            """
            You are Horizon Tours & Travel's AI assistant.

            Answer ONLY from the provided context.

            Conversation History:
            {chat_history}

            Context:
            {context}

            Question:
            {input}

            

            Answer:
            """
        )

        document_chain = create_stuff_documents_chain(
            self.llm,
            prompt
        )

        self.chain = create_retrieval_chain(
            self.retriever,
            document_chain
        )

    def ask(self, question, history):

        response = self.chain.invoke(
            {
                "input": question,
                "chat_history": "\n".join(history)
            }
        )

        sources = []

        if "context" in response:

            sources = list(
                {
                    doc.metadata.get(
                        "source",
                        "Unknown"
                    )
                    for doc in response["context"]
                }
            )

        return {
            "answer": response["answer"],
            "sources": sources
        }


rag_service = RAGService()