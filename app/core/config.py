from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PDF_PATH = "data\Horizon_Tours_Complete_Knowledge_Base_2025.pdf"

CHROMA_PATH = "chroma_db"

MODEL_NAME = "llama-3.3-70b-versatile"

GROQ_BASE_URL = "https://api.groq.com/openai/v1"