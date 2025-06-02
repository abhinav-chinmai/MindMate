from app.core.constants import PROMPT
import requests

def run_llm(prompt=PROMPT, summary=None):
    print('Receiving response from LLaMA...')
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": f"{prompt}, {summary}" if summary else prompt,
            "stream": False
        }
    )
    print(f"status code: {response.status_code}")
    llama_response = response.json().get("response", "No response from LLaMA.")
    print(llama_response)
    return llama_response
