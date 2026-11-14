from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

if not api_key or not model:
    raise ValueError("API_KEY and MODEL must be set in the environment")

client = OpenAI(
    api_key=api_key,
    base_url=base_url if base_url else None
)

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "What is AI?"}]
)

print("Response is:", response.choices[0].message.content)