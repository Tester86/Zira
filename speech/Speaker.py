import pyttsx3
import argparse

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.ap = argparse.ArgumentParser()
        self.ap.add_argument("-i", "--voice-id", help="Set different voices for Zira", type=int)
        self.args = vars(self.ap.parse_args())
        if self.args["voice_id"] not in range(len(self.engine.getProperty("voices"))):
            print(f"Error: You only have up to {len(self.engine.getProperty('voices'))} voices")
        else:
            self.change_voice(self.args["voice_id"])
    def say(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()
    def change_voice(self, id):
        self.engine.setProperty("voice", self.engine.getProperty("voices")[id].id)