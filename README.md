# Librería de doña Likor 

Este proyecto es una biblioteca modular en Python diseñada para procesar consultas académicas mediante texto o voz. Utiliza una arquitectura de pipeline de lenguaje que incluye un tokenizador (Lexer), un analizador sintáctico (Parser) y un motor de Inteligencia Artificial (Gemini/OpenRouter) para generar respuestas personalizadas.
## Características 
Entrada Dual: Soporta consultas escritas y comandos de voz (STT).

Procesamiento Gramatical: Incluye un lenguaje de comandos propio para definir acciones, temas y parámetros específicos.

IA Multi-Modelo: Integración con Google Gemini 2.5 Flash y respaldo (fallback) con OpenRouter.

Salida Versátil: Capacidad de responder en texto plano o generar archivos de audio (TTS).

Normalización Inteligente: Convierte el lenguaje natural hablado en comandos estructurados válidos para el parser.

## Estructura del Proyecto 

El proyecto se organiza en tres módulos principales:

### 1. Audio

```bash
stt.py: Maneja el reconocimiento de voz utilizando SpeechRecognition.

tts.py: Convierte las respuestas de texto a audio usando gTTS.

normalizador.py: Transforma el texto bruto del micrófono en una cadena con formato compatible: accion : "tema" (parametros).
```

### 2. Gramática

```bash
lexer.py: Realiza el análisis léxico, identificando tokens como ACCION, PARAMETRO, VALOR, etc.

parser.py: Valida la estructura sintáctica de los tokens y extrae la lógica de la consulta.
```


### 3. IA

```bash
gemini.py: Cliente para la API de Google Generative AI.

openRouter.py: Cliente de respaldo compatible con OpenAI para modelos gratuitos de OpenRouter.

ia.py: Clase controladora que gestiona la redundancia entre modelos de IA.

promptBuilder.py: Construye prompts estructurados siguiendo un rol de asistente académico.
```
## Instalación
1 Clona el repositorio.

2 Instala las dependencias necesarias:
```bash
pip install google-genai openai-python python-dotenv SpeechRecognition gTTS PyAudio
```
3 Configura tus variables de entorno en un archivo .env:
```bash
GEMINI_API_KEY=tu_api_key_aqui
OPENROUTER_API_KEY=tu_api_key_aqui
```
## Uso de la Gramática
El sistema responde a una estructura específica para procesar las peticiones:

Formato:
ACCION : "CONTENIDO" (tipo = "audio/texto", parametro = "valor")

Ejemplo de consulta manual:

```bash
libreria.procesarConsulta('Explicar : "Leyes de Newton" (tipo = "texto", tono = "formal")')
```
Ejemplo mediante voz:
Al hablar, el Normalizador se encarga de estructurar la frase para que el Parser pueda entenderla. Solo necesitas decir la acción, el tema y los parámetros clave (obligatoriamente el "tipo").

## Ejemplo de implementacion 
```bash
from libreria import Libreria

# Inicializar la librería
app = Libreria()

# Caso 1: Procesar consulta por voz
try:
    resultado = app.escucharConsulta()
    # Si tipo es "audio", devuelve un objeto BytesIO
    # Si tipo es "texto", devuelve un string
    print(resultado)
except Exception as e:
    print(f"Error: {e}")
```

## Parámetros Soportados

### Parámetros de Consulta

| Parámetro | Descripción | Valores por defecto |
| :--- | :--- | :--- |
| **tipo** | **(Obligatorio)** Define el formato de salida de la respuesta. | `audio`, `texto` |
| **idioma** | Define el idioma en el que responderá la IA. | `español` |
| **tono** | Define el estilo de comunicación del asistente. | `neutral` |
| **longitud** | Define qué tan extensa será la respuesta generada. | `media` |
| **contexto** | Permite añadir información adicional para guiar la respuesta. | `sin contexto adicional` |

