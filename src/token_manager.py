
import tiktoken

from src.config import OPENAI_MODEL


def count_tokens(text):
    try:
        encoding = tiktoken.encoding_for_model(OPENAI_MODEL)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))


def estimate_tokens(text):
    tokens = count_tokens(text)

    return {
        "token_count": tokens,
        "estimated_input_cost_note": (
            "Actual API cost depends on the model's current pricing "
            "and any additional input tokens."
        ),
    }
