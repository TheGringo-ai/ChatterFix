import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

MODEL_PRICES = {
    "gpt-4o": {"input": 0.0025, "output": 0.005},
    "gpt-4.1": {"input": 0.0020, "output": 0.008},
    "gpt-4.1-mini": {"input": 0.0004, "output": 0.0016},
    "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
}

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def run_chat(model: str, task: str, user_input: str):
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": f"You are an AI assistant helping with task: {task}."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content
    usage = response.usage

    # ✅ Correct token-based pricing math
    cost = (
        usage.prompt_tokens * MODEL_PRICES[model]["input"] / 1000 +
        usage.completion_tokens * MODEL_PRICES[model]["output"] / 1000
    )

    return result, round(cost, 6), usage