#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

"""
Class for the nodes of the AST
"""


class Node:
    # List of Nodes.
    __children = []

    # Token Class from the parser.
    token = ""

    # Initialize the node with the children and the original token from the parser.
    def __init__(self):
        self.__children = []
        self.token = ""

    # Setters and Getters
    def getChildren(self):
        return self.__children

    def setChildren(self, children):
        self.__children = children

    def getToken(self):
        return self.token

    def setToken(self, token):
        self.token = token

    def show(self):
        print("TokenClass: ", self.token)
        print("Children: ", self.__children)

    def __str__(self):
        return self.token


class Def(Node):
    pass


class Sino_statement(Node):
    pass


class If(Node):
    pass


class Else(Node):
    pass


class For(Node):
    pass


class En_Caso(Node):
    pass


class Cuando_statement(Node):
    pass


class EnTons_statement(Node):
    pass


class Set(Node):
    pass


class Assignment(Node):

    def __init__(self):
        Node.__init__(self)

    pass


class BoolOp(Node):
    pass


class Metronomo(Node):
    pass


class Vibrato(Node):
    pass


class Negation(Node):
    pass


class Abanico(Node):
    pass


class Print(Node):
    pass


class Vertical(Node):
    pass


class Percutor(Node):
    pass


class Golpe(Node):
    pass


class Expression(Node):
    __operator = ""

    def __init__(self, operator):
        Node.__init__(self)
        self.__operator = operator

    def setOperator(self, operator):
        self.__operator = operator

    def getOperator(self):
        return self.__operator

    def hasOperator(self):
        return self.__operator != ""
