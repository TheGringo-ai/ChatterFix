import os
import requests
import logging

class GeminiAIService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.api_url = "https://generativelanguage.googleapis.com/v1beta3/models/gemini-pro:generateContent"

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is required. Set it in env or pass it explicitly.")

    def ask(self, prompt: str, system_prompt: str = None) -> str:
        """Send a prompt to Gemini and return the response text."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Optional system prompt
        parts = []
        if system_prompt:
            parts.append({"text": system_prompt})
        parts.append({"text": prompt})

        payload = {
            "contents": [{"parts": parts}]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            logging.error(f"Gemini API error: {e}")
            return "⚠️ Gemini failed to generate a response."

    def ask_json(self, prompt: str, system_prompt: str = None) -> dict:
        """Attempt to parse Gemini output as JSON."""
        try:
            text = self.ask(prompt, system_prompt=system_prompt)
            return eval(text) if text.startswith("{") else {"raw": text}
        except Exception as e:
            return {"error": str(e)}
