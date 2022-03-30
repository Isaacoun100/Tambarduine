import Lexer
from sly import Parser

"""
Class for the parser
"""


class CalcParser(Parser):
    debugfile = 'parser.out'
    tokens = Lexer.CalcLexer.tokens

    def __init__(self):
        self.names = {}

    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr
        return ('assignment', p.NAME, p.expr)

    # ********************************* EXPRESSION *********************************#

    # DEFINITION OF EXPRESSION  **TERMINAL**
    @_('expr')
    def statement(self, p):

        return p.expr

    # ********************************* STATEMENTS *********************************#

    # TODO: CASO CUANDO EL STATEMENT ES EMPTY
    # TODO: IMPLEMENTAR RECURSIVIDAD <STATEMENTS> = <STATEMENTS><STATEMENTS>
    # TODO: AGREGAR EL BLOQUE DE STATEMENTS BRACKET STATEMENTS BRACKET (SIMPLIFICACION DEL CODIGO)

    # SET statement
    @_('SET NAME expr SEMI')
    def statement(self, p):
        return ('SET_VAR', p.NAME, p.expr)

    # IF statement
    @_('IF LPAREN expr RPAREN LBRACE statement RBRACE Else')
    def statement(self, p):
        return ('IF_EXPRESSION', p.expr, p.statement, p.Else)

    # ELSE statement
    @_('ELSE  LBRACE statement RBRACE')
    def Else(self, p):
        return ('ELSE_EXPRESSION', p.statement)

    # FOR statement
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN STEP LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        return ('FOR_EXPRESSION', p[2], p[6], p[10], p.statement)

    # FOR statement NO STEP
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        return ('FOR_EXPRESSION', p[2], p[6], 1, p.statement)

    # En Caso <identifier>
    @_('EN_CASO NAME Cuando')
    def statement(self, p):
        return ('EnCaso', p.NAME, p.Cuando)

    # Cuando < relational operator> < ID | INTEGER > En tons <statements>
    @_('CUANDO LT NUMBER EnTons')
    def Cuando(self, p):
        return ('Cuando', p[1], p.NUMBER, p.EnTons)

    # En tons <statemetns> Sino <statements> Fin En caso |En tons <statemetns> Cuando <statements>
    @_('EN_TONS LBRACE statement RBRACE Cuando')
    def EnTons(self, p):
        return ('EnTons-Cuando', p.statement, p.Cuando)

    # En tons <statemetns> Sino <statements> Fin En caso |En tons <statemetns> Cuando <statements>
    @_('EN_TONS LBRACE statement RBRACE Sino')
    def EnTons(self, p):
        return ('EnTons-Fin', p.statement, p.Sino)

    # Si No
    @_('SI_NO LBRACE statement RBRACE FIN_EN_CASO')
    def Sino(self, p):
        print("Not implemented, SINO")
        return ('sino', p.statement)

    # def statement
    @_('DEF NAME LPAREN RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        return ('DEF_STATEMENT', p.NAME, p.statement)

    # ********************************* INCLUDED FUNCTIONS *********************************#
    # TODO: ADD "DEF" SYNTAX
    # TODO: AGREGAR PRODUCCIONES PARA PARAMETROS DE DEF
    # TODO: AGREGAR PARAMETRO PRINCIPAL
    # TODO: test

    # Abanico A - B
    @_('ABANICO LPAREN LETTER_B RPAREN SEMI',
       'ABANICO LPAREN LETTER_A RPAREN SEMI')
    def statement(self, p):
        return ('ABANICO_STATEMENT', p[2])

    # Vertical
    @_('VERTICAL LPAREN LETTER_I RPAREN SEMI',
       'VERTICAL LPAREN LETTER_D RPAREN SEMI')
    def statement(self, p):
        return ('VERTICAL_STATEMENT', p[2])

    # PERCUTOR SIMPLE
    @_('PERCUTOR LPAREN LETTER_A RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_B RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_D RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_I RPAREN SEMI')
    def statement(self, p):
        return ('PERCUTOR_STATEMENT', p[2])

    # PERCUTOR AMBOS LADOS
    @_(
        'PERCUTOR LPAREN LETTER_A LETTER_B RPAREN SEMI',
        'PERCUTOR LPAREN LETTER_D LETTER_I RPAREN SEMI', )
    def statement(self, p):
        return ('PERCUTOR_STATEMENT', p[2] + p[3])

    # GOLPE
    @_('GOLPE LPAREN RPAREN SEMI')
    def statement(self, p):
        return ('GOLPE_STATEMENT', 1)

    # VIBRATO
    @_('VIBRATO LPAREN NUMBER RPAREN SEMI')
    def statement(self, p):
        return ('VIBRATO_STATEMENT', p.NUMBER)

    # METRONOMO
    @_('METRONOMO LPAREN LETTER_A RPAREN SEMI',
       'METRONOMO LPAREN LETTER_D RPAREN SEMI')
    def statement(self, p):
        return ('METRONOMO_STATEMENT', p[2])

    # PRINT
    @_('PRINT LPAREN STRING RPAREN SEMI',
       'PRINT LPAREN NAME RPAREN SEMI',
       'PRINT LPAREN expr RPAREN SEMI',
       'PRINT LPAREN NUMBER RPAREN SEMI')
    def statement(self, p):
        return ('PRINT_STATEMENT', p[2])

    # FALSE - TRUE OPERATORS
    @_('NAME PERIOD LETTER_T SEMI')
    def statement(self, p):
        return ('BOOLAN_OP', p.NAME, 1)

    @_('NAME PERIOD LETTER_F SEMI')
    def statement(self, p):
        return ('BOOLAN_OP', p.NAME, 0)

    # NEGATION
    @_('NAME PERIOD NEGATION SEMI')
    def statement(self, p):
        return ('BOOLEAN_NEGATION', p.NAME)

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
    text = 'EN_CASO @var CUANDO < 2  EN_TONS { DEF @metodo(){@var = 666} } CUANDO < 5  EN_TONS { @var = 2 } SI_NO{ @var = 5 } FIN_EN_CASO '
    print(parser.parse(lexer.tokenize(text)))
