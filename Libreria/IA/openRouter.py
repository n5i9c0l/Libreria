from openai import OpenAI

class OpenRouter:
    def __init__(self):
        self.modelo  ="openrouter/free"
        self.cliente = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")

    def generar(self, prompt):
        respuesta = self.cliente.chat.completions.create(
            model=self.modelo,
            messages=[{"role": "user", "content": prompt}]
        )
        return respuesta.choices[0].message.content

ia = OpenRouter()
print(ia.generar("¿Cuál es la capital de Francia?"))