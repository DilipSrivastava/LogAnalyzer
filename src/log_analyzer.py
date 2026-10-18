from src.llm_client import analyze_with_llm
from src.prompt_builder import build_log_analysis_prompt
from src.token_manager import count_tokens
from src.sensitive_data_masker import mask_sensitive_data


def analyze_log(log_content):
    masked_log_content = mask_sensitive_data(log_content)

    system_prompt, user_prompt = build_log_analysis_prompt(masked_log_content)
    total_input_tokens = count_tokens(system_prompt + user_prompt)

    result = analyze_with_llm(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        temperature=0.2,
    )

    result["estimated_input_tokens"] = total_input_tokens
    result["sensitive_data_masked"] = masked_log_content != log_content
    result["masked_log_content"] = masked_log_content

    return result