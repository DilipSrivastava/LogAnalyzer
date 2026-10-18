
import re


def mask_sensitive_data(text: str) -> str:
    # Mask JSON-style and plain-text password fields
    text = re.sub(
        r'''(?i)(["']?(?:password|passwd|pwd)["']?\s*[:=]\s*)("[^"]*"|'[^']*'|[^,\s}]+)''',
        r'\1"***MASKED***"',
        text,
    )

    # Mask API keys, access tokens and secret keys
    text = re.sub(
        r'''(?i)(["']?(?:api[_-]?key|access[_-]?token|secret[_-]?key)["']?\s*[:=]\s*)("[^"]*"|'[^']*'|[^,\s}]+)''',
        r'\1"***MASKED***"',
        text,
    )

    # Mask bearer tokens and JWTs
    text = re.sub(
        r'(?i)(\bBearer\s+)[A-Za-z0-9._~+/-]+=*',
        r'\1"***MASKED***"',
        text,
    )

    text = re.sub(
        r'\beyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*\b',
        '"***MASKED***"',
        text,
    )

    # Mask email addresses
    text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        '"Email":"***MASKED***"',
        text,
    )

    # Mask IPv4 addresses
    text = re.sub(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        '"ClientIP":"***MASKED***"',
        text,
    )

    # Mask credit-card-like numbers
    text = re.sub(
        r'\b(?:\d[ -]*?){13,19}\b',
        '"CreditCard":"***MASKED***"',
        text,
    )

    return text
