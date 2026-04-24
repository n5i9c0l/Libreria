from google import genai

class Ia:

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generar(self, prompt):
        respuesta = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return respuesta.text


    
gemini = Ia("AIzaSyAXExckvE9oSwxCghNwha8fTYXF7oDW4l0")
print(gemini.generar("¿Cuál es la capital de Francia?"))