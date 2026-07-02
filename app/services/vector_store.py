import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from app.core.config import (
    PDF_PATH,
    CHROMA_PATH
)


class VectorStoreManager:

    def __init__(self):
        self.embeddings = FastEmbedEmbeddings()

    def load_documents(self):

        if not os.path.exists(PDF_PATH):
            raise FileNotFoundError(
                f"PDF not found: {PDF_PATH}"
            )

        loader = PyPDFLoader(PDF_PATH)

        return loader.load()

    def split_documents(self, docs):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        return splitter.split_documents(docs)

    def create_store(self):

        docs = self.load_documents()

        chunks = self.split_documents(docs)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=CHROMA_PATH
        )

        return vector_store

    def get_store(self):

        if os.path.exists(CHROMA_PATH):

            return Chroma(
                persist_directory=CHROMA_PATH,
                embedding_function=self.embeddings
            )

        return self.create_store()

    def get_retriever(self):

        store = self.get_store()

        return store.as_retriever(
            search_kwargs={"k": 5}
        )


manager = VectorStoreManager()


def get_retriever():
    return manager.get_retriever()