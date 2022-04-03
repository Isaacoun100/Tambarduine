#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from Sintactic_Analysis.Parser import *
from AST.AbstractSyntaxTree import *
from Messages import Message as msg

msgs = msg.Message()


class Comp:
    __lexer = Lexer.CalcLexer()
    __parser = CalcParser()

    def compile(self, code):
        tokenize = self.__lexer.tokenize(code)
        node = (self.__parser.parse(tokenize))
        ast = AST(node)

        # if len(msgs.getMessages()) == 0:
        #     print("No errors")
        # for e in msgs.getMessages():
        #     print("Mensage: ", e.getBody())
        return ast
