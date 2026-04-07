from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

# 🔑 Replace with your OpenRouter API key
API_KEY = "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"

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request structure
class CodeRequest(BaseModel):
    code: str
    input_language: str
    output_language: str


@app.post("/optimize")
async def optimize_code(request: CodeRequest):

    prompt = f"""
Convert the following {request.input_language} code into {request.output_language} and optimize it.

IMPORTANT:
Return ONLY the final code.
Do NOT explain anything.
Do NOT include headings.
Do NOT include markdown formatting.

Code:
{request.code}
"""

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/auto",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        # API error handling
        if "error" in data:
            return {
                "optimized_code": f"API Error: {data['error']['message']}"
            }

        if "choices" not in data:
            return {
                "optimized_code": f"Unexpected API response: {data}"
            }

        optimized_code = data["choices"][0]["message"]["content"]

        return {
            "optimized_code": optimized_code.strip()
        }

    except Exception as e:
        return {
            "optimized_code": f"Server Error: {str(e)}"
        }