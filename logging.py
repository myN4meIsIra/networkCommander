# logging
"""
implementations for logging
"""

class Logging:
    def __init__(self, logging):
        self.logging = logging
        if logging:
            self.say('logging active', "Logging")


    def say(self, text):
        print(f"\033[92m {text}\033[00m")
        return 1


    def log(self, text, classItsFrom):
        if self.logging:
            print(f' <{classItsFrom}>-- \033[93m {text}\033[00m ')
        else:
            return 1


    def error(self, text, classItsFrom):
        print(f' <{classItsFrom}>-- \033[91m {text}\033[00m')