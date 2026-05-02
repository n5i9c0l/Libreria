class Normalizador:

    PARAMETROS = {
        "tipo",
        "idioma",
        "contexto",
        "restricciones",
        "forma",
        "tono",
        "longitud"
    }

    def normalizar(self, texto):
        if texto is None or texto.strip() == "":
            raise Exception("No hay texto para normalizar")

        palabras = texto.lower().split()

        accion = palabras[0]

        contenido = []
        parametros = {}

        i = 1

        while i < len(palabras):
            palabra = palabras[i]

            if palabra in self.PARAMETROS:
                parametro = palabra
                i += 1

                valor = []

                while i < len(palabras) and palabras[i] not in self.PARAMETROS:
                    valor.append(palabras[i])
                    i += 1

                parametros[parametro] = " ".join(valor)

            else:
                contenido.append(palabra)
                i += 1

        if "tipo" not in parametros:
            raise Exception('Debe indicar el parámetro "tipo"')

        if parametros["tipo"] not in {"audio", "texto"}:
            raise Exception('El parámetro "tipo" solo puede ser "audio" o "texto"')

        contenidoFinal = " ".join(contenido)

        opciones = []
        for clave, valor in parametros.items():
            opciones.append(f'{clave} = "{valor}"')

        opcionesFinal = ", ".join(opciones)

        return f'{accion} : "{contenidoFinal}" ({opcionesFinal})'