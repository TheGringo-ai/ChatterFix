import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_code(task: str, context: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You are an expert Python/TypeScript developer."},
            {"role": "user", "content": f"Task: {task}\n\nContext:\n{context}"}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content