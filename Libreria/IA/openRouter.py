from openai import OpenAI
from dotenv import load_dotenv as load
import os

class OpenRouter:
    def __init__(self):
        load()
        openrouter_key = os.getenv("OPENROUTER_API_KEY")
        self.modelo  ="openrouter/free"
        self.cliente = OpenAI(api_key=openrouter_key, base_url="https://openrouter.ai/api/v1")

    def generar(self, prompt):
        respuesta = self.cliente.chat.completions.create(
            model=self.modelo,
            messages=[{"role": "user", "content": prompt}]
        )
        return respuesta.choices[0].message.content

