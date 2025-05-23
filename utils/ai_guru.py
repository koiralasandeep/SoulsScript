# ai_guru.py (Spiritual AI backend logic)
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_spiritual_response(user_input):
    messages = [
        {"role": "system", "content": "You are SoulScript, a wise and loving spiritual guide. Respond calmly, share a verse from the Bhagavad Gita and Bible, explain them, and provide comfort."},
        {"role": "user", "content": f"The user says: {user_input}\n\nRespond with:\n1. Empathetic explanation\n2. One relevant Gita verse with explanation\n3. One relevant Bible verse with explanation\n4. Apply the verses to the user's situation\n5. Ask a gentle follow-up"}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

