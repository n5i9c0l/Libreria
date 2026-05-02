import re

class Tokenizador:
    def __init__(self):
        self.patron = r'[a-zA-Z]+|"[^"]*"|[:(),=]'
        self.parametros = {"tipo", "idioma", "contexto", "restricciones", "tono", "longitud"}

    def tokenizar(self, texto):
        texto_token = re.findall(self.patron, texto)
        tokens = []

        for parte in texto_token:
            if parte == ":":
                tokens.append(("DOS_PUNTOS", parte))
            elif parte == ",":
                tokens.append(("COMA", parte))
            elif parte == "(":
                tokens.append(("PARENTESIS_ABIERTO", parte))
            elif parte == ")":
                tokens.append(("PARENTESIS_CERRADO", parte))
            elif parte == "=":
                tokens.append(("IGUAL", parte))
            elif parte in self.parametros:
                tokens.append(("PARAMETRO", parte))
            elif parte.startswith('"') and parte.endswith('"'):
                tokens.append(("VALOR", parte[1:-1]))
            else:
                raise Exception(f"Palabra no permitida: {parte}")
        return tokens