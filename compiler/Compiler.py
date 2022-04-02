#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from Parser import *
from AST.AbstractSyntaxTree import *


class Compiler:
    def compile(self, text):
        lexer = Lexer.CalcLexer()
        parser = CalcParser()
        # text = 'EN_CASO @var CUANDO < 2  EN_TONS { DEF @metodo(){@var1 = 666} } CUANDO < 5  EN_TONS { @var2 = 2 } SI_NO{ @var3 = 5 } FIN_EN_CASO '
        # text = 'IF(243 < 23){@var = 23} ELSE{ @VAR3 = 38}'
        node = (parser.parse(lexer.tokenize(text)))
        ast = AST(node)

        return ast


if __name__ == '__main__':
    comp = Compiler()
    text = 'EN_CASO @var CUANDO < 2  EN_TONS { DEF @metodo(){@var1 = 666} } CUANDO < 5  EN_TONS { @var2 = 2 } SI_NO{ @var3 = 5 } FIN_EN_CASO '

    ast = comp.compile(text)
    ast.print()
