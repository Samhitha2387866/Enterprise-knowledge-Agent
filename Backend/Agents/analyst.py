import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

DEFAULT_CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-4-8")

def generate_answer(context, question):
    response = client.messages.create(
        model=DEFAULT_CLAUDE_MODEL,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""
                Use only the given documents to answer.
                Documents:{context}
                Question:{question}
                Give a concise and accurate answer based on the documents. If the answer is not present in the documents, respond with 'I don't know'."""
            }
        ],
    )
    return response.content[0].text