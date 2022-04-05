#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.
from compiler.Messages.Output import Output


class Error(Output):
    __line: int

    def __init__(self, line):
        self.__line = line
        Output.__init__(self)

    def getLine(self) -> int:
        return self.__line

    def setLine(self, line: int):
        self.__line = line
