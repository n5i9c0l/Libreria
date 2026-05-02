import speech_recognition as sr
import pyttsx3
class Audio:
    def __init__(self):
        self.reconocedor = sr.Recognizer()
        self.motor = pyttsx3.init()

    def escuchar(self):
        with sr.Microphone() as source:
            print("Empiece a realizar el dictado:")
            audio = self.reconocedor.listen(source)
        try:
            text = self.reconocedor.recognize_google(audio)
            print("Dijiste: "+text)
            return text
        except sr.UnknownValueError:
            print("No puedo entender el audio.")
            return None
        except sr.RequestError as e:
            print("Error en los resultados")
            return None
        
    def hablar(self, texto):
        self.motor.setProperty('rate', 167)#sixeseven referencia
        self.motor.say(texto)
        self.motor.runAndWait()
