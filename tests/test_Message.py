#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from unittest import TestCase
from Messages.Message import *
from Messages.Output import *
from Messages.Print import *
from Messages.Error import *


class TestMessage(TestCase):
    __msg = Message()
    __error1 = Error()
    __error1.setBody("Error en la definicion de la variable")
    __error1.setLine(23)

    __error2 = Error()
    __error2.setBody("';' faltante")
    __error2.setLine(3)

    __print1 = Print()
    __print1.setBody("Hola mundo")
    __print2 = Print()
    __print2.setBody("Adios Mundo")

    def test_set_messages(self):
        self.__msg.setMessages([self.__error2, self.__error1, self.__print2, self.__print1])

    def test_get_messages(self):
        self.__msg.addOutput(self.__error1) \
            .addOutput(self.__error2) \
            .addOutput(self.__print1) \
            .addOutput(self.__print2)
        for i in self.__msg.getMessages():
            print("Output: ", i)

    def test_add_output(self):
        self.__msg.addOutput(self.__error1) \
            .addOutput(self.__error2) \
            .addOutput(self.__print1) \
            .addOutput(self.__print2)
