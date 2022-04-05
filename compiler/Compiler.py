#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from compiler.Sintactic_Analysis.Parser import *
from compiler.AST.AbstractSyntaxTree import *
from compiler.Messages import Message as msg
from compiler.CodeGenerator import *

msgs = msg.Message()


class Comp:
    __lexer = Lexer.CalcLexer()
    __parser = CalcParser()
    __codeGenerator = CodeGenerator()

    def compile(self, code):
        tokenize = self.__lexer.tokenize(code)
        node = (self.__parser.parse(tokenize))
        ast = AST(node)
        result = self.__codeGenerator.compile(ast)
        return result
