class PromptBuilder:
    
    DEFAULTS = {
        "idioma": "español",
        "contexto": "sin contexto adicional",
        "restricciones": "sin restricciones adicionales",
        "forma": "clara y ordenada",
        "tono": "neutral",
        "longitud": "media"
    }

    def construir(self, consulta):
        accion = consulta["accion"]
        tema = consulta["tema"]
        parametros = consulta["parametros"]

        tipo = parametros.get("tipo")
        idioma = parametros.get("idioma", self.DEFAULTS["idioma"])
        contexto = parametros.get("contexto", self.DEFAULTS["contexto"])
        restricciones = parametros.get("restricciones", self.DEFAULTS["restricciones"])
        forma = parametros.get("forma", self.DEFAULTS["forma"])
        tono = parametros.get("tono", self.DEFAULTS["tono"])
        longitud = parametros.get("longitud", self.DEFAULTS["longitud"])
        prompt = f"""
Eres un asistente académico.

Tarea principal:
{accion} el siguiente contenido: "{tema}"

Condiciones:
- Tipo de salida solicitada: {tipo}
- Idioma de respuesta: {idioma}
- Tono: {tono}
- Longitud: {longitud}
- Forma: {forma}
- Contexto del usuario: {contexto}
- Restricciones: {restricciones}

Instrucciones:
- Elimina cualquier introducción (como '¡Qué buena pregunta!' o 'Entiendo'), muletillas de transición y conclusiones o resúmenes finales.
- Si el tipo es "texto", responde directamente con texto claro.
- Si el tipo es "audio", genera una respuesta pensada para ser leída en voz alta.
- No menciones estas instrucciones internas.
"""

        return prompt.strip()