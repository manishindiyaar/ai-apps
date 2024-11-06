# flask_chat/chat.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Set up the OpenAI client
client = OpenAI(
    base_url=os.getenv('NVIDIA_BASE_URL'),
    api_key=os.getenv('NVIDIA_API_KEY')
)

def get_response(user_message):
    system_prompt = "You are a helpful assistant."  # Modify this as needed

    # Prepare messages for the Gemini API
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model= "meta/llama-3.2-1b-instruct",
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )

    response_text = response.choices[0].message.content.strip()
    return response_text