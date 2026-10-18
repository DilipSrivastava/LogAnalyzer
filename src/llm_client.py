
from openai import OpenAI
from src.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_with_llm(system_prompt, user_prompt, temperature=0.2):
    #sends a request to the OpenAI API to get a response from an LLM
    response = client.chat.completions.create( 
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )

    return {
        "content": response.choices[0].message.content,
        "model": response.model,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
    }
