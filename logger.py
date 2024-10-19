# logging
"""
implementations for logging
"""

class DataLogging:
    def __init__(self, logging):
        self.logging = logging
        if logging:
            self.say('logging active')


    def say(self, text):
        print(f"\033[92m {text}\033[00m")
        return 1


    def log(self, text, classItsFrom):
        if self.logging:
            print(f'\033[93m <{classItsFrom}>--  {text}\033[00m ')
        else:
            return 1


    def error(self, text, classItsFrom):
        print(f'\033[91m <{classItsFrom}>--  {text}\033[00m')