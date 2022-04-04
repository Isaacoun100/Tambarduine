#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.
from AST.Node import *


class AST:
    __root = None

    def __init__(self, root):
        self.__root = root

    def setRoot(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

    # node: nodo para recorrer
    # flag: una lista de booleans para saber cuales revise
    # depth: nivel del nodo
    # is last: si el nodo es el ultimo
    def __printNTree(self, node, flag, depth, isLast):
        # caso base
        if node == None:
            return

        for i in (range(1, depth)):
            if flag[i]:
                print("| ", "", "", "", end="")
                # Otherwise print
                # the blank spaces
            else:
                print(" ", "", "", "", end="")

        # Condition when the current
        # node is the root node
        if depth == 0:

            print(node.token)

        # Condition when the node is
        # the last node of
        # the exploring depth
        elif isLast:
            string = ""
            if isinstance(node, type(Node)):
                string = node.token
            else:
                string = str(node)
            print("+---", string)

            # No more childrens turn it
            # to the non-exploring depth
            flag[depth] = False
        else:
            string = ""
            if isinstance(node, type(Node)):
                string = node.token
            else:
                string = str(node)
            print("+---", string)

        if isinstance(node, Node):

            it = 0
            for i in node.getChildren():
                it += 1

                # Recursive call for the
                # children nodes
                self.__printNTree(i, flag, depth + 1, it == (len(node.getChildren()) - 1))
            flag[depth] = True

    def print(self):
        flag = [True] * 100
        self.__printNTree(self.__root, flag, 0, False)
