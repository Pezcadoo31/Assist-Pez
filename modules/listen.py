import speech_recognition as sr

r = sr.Recognizer()


class Listener:
    def listen(self):
        with sr.Microphone() as source:    
            print("Diga algo:")
            audio = r.listen(source)
            print("Reconociendo...")
            try:
                audio_text = r.recognize_google(audio, language='es-ES')
                print("Texto: {}".format(audio_text))
                return audio_text
            except:
                print("Lo siento, no te entiendo")


