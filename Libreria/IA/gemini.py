from google import genai
from dotenv import load_dotenv as load
import os

class Ia:
    def __init__(self):
        load()
        gemini_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=gemini_key)

    def generar(self, prompt):
        respuesta = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return respuesta.text

gemini = Ia()
print(gemini.generar("¿Cuál es la capital de Francia?"))