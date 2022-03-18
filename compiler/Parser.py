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

    # ********************************* STATEMENTS *********************************#
    @_('expr')
    def statement(self, p):
        return p.expr

    # SET statement
    @_('SET NAME expr SEMI')
    def statement(self, p):
        return ('SET_VAR', p.NAME, p.expr)

    # IF statement
    @_('IF LPAREN expr RPAREN LBRACE statement RBRACE Else')
    def statement(self, p):
        return ('IF_EXPRESSION', p.expr, p.statement, p.Else)

    # ELSE statement
    @_('ELSE  LBRACE expr RBRACE')
    def Else(self, p):
        return ('ELSE_EXPRESSION', p.expr)

    # FOR statement
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN STEP LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        return ('FOR_EXPRESSION', p[2], p[6], p[10], p.statement)

    # FOR statement NO STEP
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        return ('FOR_EXPRESSION', p[2], p[6], 1, p.statement)

    # *********************************  Expression Operator Expression  ********************************* #
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
    text = 'FOR (12)  TO  (39) {IF(3>3){SET @var 3;} ELSE { 303 + 3}}'
    print(parser.parse(lexer.tokenize(text)))
