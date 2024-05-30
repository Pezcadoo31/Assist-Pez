import pyttsx3

engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


class Talker:
    
    def talk(self, text):
        engine.say(text)
        engine.runAndWait()


