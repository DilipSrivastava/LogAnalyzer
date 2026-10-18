
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

MAX_LOG_FILE_SIZE_MB = 5
MAX_LOG_FILE_SIZE_BYTES = MAX_LOG_FILE_SIZE_MB * 1024 * 1024

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Please configure it in .env")
