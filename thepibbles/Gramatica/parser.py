class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.tipos = {"texto", "audio"}

    def getActual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return None
    
    def revisar(self, tipo):
        token = self.getActual()
        
        if token is None:
            raise Exception(f"Se esperaba un token de tipo {tipo} pero se encontró el final de la entrada")
        
        tipoActual, valor = token
        if tipoActual == tipo:
            self.pos += 1
            return valor
        else:
            raise Exception(f"Se esperaba un token de tipo {tipo} pero se encontró {tipoActual}")
        
    def parsear(self):
        accion = self.revisar("ACCION")
        self.revisar("DOS_PUNTOS")
        tema = self.revisar("VALOR")
        self.revisar("PARENTESIS_ABIERTO")
        parametros = self.parsearParametros()
        self.revisar("PARENTESIS_CERRADO")

        return {"accion": accion, "tema": tema, "parametros": parametros}

    def parsearParametros(self):
        parametros = {}
        parametro = self.revisar("PARAMETRO")

        if parametro != "tipo":
            raise Exception(f"El primer parametro debe ser 'tipo'")
        self.revisar("IGUAL")
        valor = self.revisar("VALOR")

        if valor not in self.tipos:
            raise Exception(f"Valor no permitido para el parametro 'tipo': {valor}")
        
        parametros[parametro] = valor

        while self.getActual() is not None and self.getActual()[0] != "PARENTESIS_CERRADO":
            self.revisar("COMA")
            parametro = self.revisar("PARAMETRO")
            self.revisar("IGUAL")
            valor = self.revisar("VALOR")
            parametros[parametro] = valor

        return parametros