import speech_recognition as sr

class Audio:

    def __init__(self):
        self.reconocedor = sr.Recognizer()
        self.idioma ="es-ES"

    def escuchar(self):
        try:
            with sr.Microphone() as source:
                self.reconocedor.adjust_for_ambient_noise(source, duration=0.5)

                audio = self.reconocedor.listen(
                    source,
                    timeout=20,
                    phrase_time_limit=None
                )

            texto = self.reconocedor.recognize_google(
                audio,
                language=self.idioma
            )

            return texto.strip()

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            return None

        except sr.RequestError:
            return None
