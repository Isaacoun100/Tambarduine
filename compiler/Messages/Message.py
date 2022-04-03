#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.
from Messages.Output import Output


class Message:
    # List containing al the errors and messages generated.
    __messages = []

    def __init__(self):
        pass

    def getMessages(self):
        return self.__messages

    def setMessages(self, msgs):
        self.__messages = msgs

    def addOutput(self, output):
        if isinstance(output, Output):
            self.__messages.append(output)
            return self


