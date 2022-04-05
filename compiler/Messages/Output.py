#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

class Output:
    __body: str

    def setBody(self, string: str):
        self.__body = string

    def getBody(self) -> str:
        return self.__body

    def __str__(self):
        return self.__body
