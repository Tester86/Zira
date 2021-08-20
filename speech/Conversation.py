from Listener import Listener
from Speaker import Speaker
from CHandler import CHandler

class Conversation:
    def __init__(self):
        self.listener = Listener()
        self.speaker = Speaker()
        self.CHandler = CHandler()
    def polling(self): ### Designed to be embedded in a while loop
        query = self.listener.listen()
        if self.CHandler.is_command(query):
            self.speaker.say(self.CHandler.handle(query))
            return True
        ### Assuming no words of the query are in the command list
        self.speaker.say("Sorry, I don't understand. Please read the commands available")
        return False
            
a = Conversation()
a.polling()