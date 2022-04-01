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
    def __init__(self, children=None, token=""):
        if children is None:
            children = []

        self.__children = children
        self.token = token

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
