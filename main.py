import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Optional: import both AI SDKs
import openai
import google.generativeai as genai

# Load API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
AI_DEFAULT_MODEL = os.getenv("AI_DEFAULT_MODEL", "openai")

openai.api_key = OPENAI_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

def ask(prompt: str, model: str = None) -> dict:
    model = model or AI_DEFAULT_MODEL
    logging.info(f"Asking [{model}]: {prompt}")

    try:
        if model == "openai":
            return _ask_openai(prompt)
        elif model == "gemini":
            return _ask_gemini(prompt)
        else:
            raise ValueError(f"Unknown model: {model}")
    except Exception as e:
        logging.warning(f"{model} failed: {e}")
        # fallback
        alt = "gemini" if model == "openai" else "openai"
        logging.info(f"Falling back to {alt}")
        try:
            return ask(prompt, model=alt)
        except Exception as err:
            return {"error": str(err)}

def _ask_openai(prompt: str) -> dict:
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {
        "response": res.choices[0].message["content"],
        "engine": "openai"
    }

def _ask_gemini(prompt: str) -> dict:
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    res = chat.send_message(prompt)
    return {
        "response": res.text,
        "engine": "gemini"
    }
