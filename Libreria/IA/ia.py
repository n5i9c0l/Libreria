from copy import error

from gemini import Gemini
from openRouter import OpenRouter


class Ia:
    
    def __init__(self):
        self.gemini = Gemini()
        self.openrouter = OpenRouter()

    def generar(self, prompt):
        try:
            return self.gemini.generar(prompt)

        except Exception:
            return self.openrouter.generar(prompt)