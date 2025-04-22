import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def extract_info(user_input):
    prompt = f"""You are an AI analyst helping users simulate policy decisions.
Given the scenario below, extract key STAKEHOLDERS, their INTERESTS, potential BIASES, and the expected DECISION PROCESS STEPS.

Return in JSON:
{{
  "stakeholders": [...],
  "issues": [...],
  "process": [...]
}}

Scenario: {user_input}"""
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    try:
        result = response.json()
        return eval(result["choices"][0]["message"]["content"])
    except Exception as e:
        return {"error": str(e), "raw": response.text}