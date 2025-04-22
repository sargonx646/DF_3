import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
EXTRACT_PROMPT = """
Given this decision description, extract the key STAKEHOLDERS, their INTERESTS, potential BIASES, and the expected DECISION PROCESS STEPS.

Return in JSON:
{
  "stakeholders": [...],
  "issues": [...],
  "process": [...]
}
"""

def extract_info(user_input):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": EXTRACT_PROMPT + user_input}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]