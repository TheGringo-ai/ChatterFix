import os
import logging
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize logger
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Correct env variable casing
)

# Core function to run chat
async def run_chat(prompt: str, model: str = "gpt-4o") -> str:
    """
    Sends a prompt to OpenAI ChatCompletion and returns the assistant's reply.
    """
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful maintenance AI assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"OpenAI API Error: {e}")
        return f"Error during OpenAI request: {str(e)}"