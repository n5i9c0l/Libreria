from gtts import gTTS
import io

class Voz:
    def volver_audio(self, texto):
        tts = gTTS(text=texto, lang='es')
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        return audio