#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from Sintactic_Analysis.Parser import *
from AST.AbstractSyntaxTree import *


class Comp:
    def compile(self, text):
        lexer = Lexer.CalcLexer()
        parser = CalcParser()
        # text = 'EN_CASO @var CUANDO < 2  EN_TONS { DEF @metodo(){@var1 = 666} } CUANDO < 5  EN_TONS { @var2 = 2 } SI_NO{ @var3 = 5 } FIN_EN_CASO '
        # text = 'IF(243 < 23){@var = 23} ELSE{ @VAR3 = 38}'
        node = (parser.parse(lexer.tokenize(text)))
        ast = AST(node)

        return ast


if __name__ == '__main__':
    comp = Comp()
    text = 'SET @var, 13;'
    text2 = 'SET @variable, (230+ 3);'

    text3 = '@var =  2;'

    #ast = comp.compile(text)
    #ast.print()

    ast2 = comp.compile(text3)
    ast2.print()


