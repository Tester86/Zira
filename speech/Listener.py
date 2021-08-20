import speech_recognition as sr

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def listen(self):
        print("a")
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                query = self.recognizer.recognize_google(audio)
                return query
            except:
                return False