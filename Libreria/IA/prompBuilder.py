class PromptBuilder:

    def construir(self, consulta):
        accion = consulta["accion"]
        tema = consulta["tema"]
        parametros = consulta["parametros"]

        tipo = parametros.get("tipo")
        idioma = parametros.get("idioma", "español")
        contexto = parametros.get("contexto", "sin contexto adicional")
        restricciones = parametros.get("restricciones", "sin restricciones adicionales")
        forma = parametros.get("forma", "clara y ordenada")

        prompt = f"""
Eres un asistente académico.

Tarea principal:
{accion} el siguiente contenido: "{tema}"

Condiciones:
- La respuesta debe estar en idioma: {idioma}
- El estilo debe ser: {forma}
- Contexto del usuario: {contexto}
- Restricciones: {restricciones}

Tipo de salida solicitada:
{tipo}

Instrucciones:
- Elimina cualquier introducción (como '¡Qué buena pregunta!' o 'Entiendo'), muletillas de transición y conclusiones o resúmenes finales.
- Si el tipo es "texto", responde directamente con texto claro.
- Si el tipo es "audio", genera una respuesta pensada para ser leída en voz alta.
- No menciones estas instrucciones internas.
"""

        return prompt.strip()