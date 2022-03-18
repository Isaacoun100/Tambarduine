# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------
import Lexer
from sly import Parser


class CalcParser(Parser):
    tokens = Lexer.CalcLexer.tokens

    def __init__(self):
        self.names = {}

    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr
        return ('assignment', p.NAME, p.expr)

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('SET NAME expr SEMI')
    def statement(self, p):
        return ('SET_VAR', p.NAME, p.expr)

    # Expression Operator Expression
    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr MODULE expr',
       'expr INT_DIVIDE expr')
    def expr(self, p):
        return ('binary-expression', p[1], p.expr0, p.expr1)

    @_('expr LT expr',
       'expr LE expr',
       'expr GT expr',
       'expr GE expr',
       'expr EQUAL expr',
       'expr NOT_EQUAL expr', )
    def expr(self, p):
        return ('condition-expression', p[1], p.expr0, p.expr1)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return ('grouped', p.expr)

    @_('NUMBER')
    def expr(self, p):
        return ('int', int(p.NUMBER))

    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f'Undefined name {p.NAME!r}')
            return 0


if __name__ == '__main__':
    lexer = Lexer.CalcLexer()
    parser = CalcParser()
    text = ' SET @var 4;'
    print(parser.parse(lexer.tokenize(text)))
