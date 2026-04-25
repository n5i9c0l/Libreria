from google import genai

class Ia:
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyBZPr1tMMvOabaZBXo2T-kD7A7Ul2NiKJI")

    def generar(self, prompt):
        respuesta = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return respuesta.text

gemini = Ia()
print(gemini.generar("¿Cuál es la capital de Francia?"))