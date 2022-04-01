#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from Node import Node


class AST:
    __root = None

    def __init__(self, root=None):
        self.__root = Node()
        self.__root = root

    def setRoot(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root
