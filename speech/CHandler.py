from datetime import datetime

class CHandler:
    def __init__(self):
        self.commands = ["time", "weather", "news"]
        self.command = None
    def is_command(self, query):
        for i in query.split(" "):
            if i in self.commands:
                self.command = i
                return True
        return False
    def handle(self, query):
        if self.command == "time":
            hour = datetime.now().hour
            minute = datetime.now().minute
            msg = f"It is {hour} and {minute} minutes"
            return msg
        elif self.command == "weather":
            pass