
from src.config import MAX_LOG_FILE_SIZE_BYTES


def load_log_file(uploaded_file):
    if uploaded_file is None:
        raise ValueError("Please upload a log file.")

    if uploaded_file.size > MAX_LOG_FILE_SIZE_BYTES:
        raise ValueError("Log file size must not exceed 5 MB.")

    try:
        content = uploaded_file.getvalue().decode("utf-8", errors="replace")
    except Exception as exc:
        raise ValueError(f"Unable to read log file: {exc}") from exc

    if not content.strip():
        raise ValueError("The uploaded log file is empty.")

    return content
