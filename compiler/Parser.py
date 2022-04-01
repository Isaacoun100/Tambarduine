#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

import Lexer
from sly import Parser

"""
Class for the parser
"""


class CalcParser(Parser):
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
        # SET NODE
        # Token: ("SET_statement, p.Name, p.expr)
        # Children: [p.Name, p.expr]
        return ('SET_statement', p.NAME, p.expr)

    # IF statement
    @_('IF LPAREN expr RPAREN LBRACE statement RBRACE Else')
    def statement(self, p):
        # todo: IF NODE
        # IF NODE
        # Token: ('IF_statement', p.expr, p.statement, p.Else)
        # Children: [p.expr, p.statement, p.Else]
        return ('IF_statement', p.expr, p.statement, p.Else)

    # ELSE statement
    @_('ELSE  LBRACE statement RBRACE')
    def Else(self, p):
        # todo: ELSE NODDE
        # ELSE Node
        # Token: ("ELSE_statement, p.statement)
        # Children: [p.statement]
        return ('ELSE_statement', p.statement)

    # FOR statement
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN STEP LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        # todo: FOR NODE
        # FOR Node
        # Token: ("FOR_statement,p[2], p[6], p[10], p.statement)
        # Children: [p[2], p[6], p[10], p.statement]
        return ('FOR_statement', p[2], p[6], p[10], p.statement)

    # FOR statement NO STEP
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        # FOR Node
        # Token: ("FOR_statement,p[2], p[6], 1, p.statement)
        # Children: [p[2], p[6], 1, p.statement]
        return ('FOR_statement', p[2], p[6], 1, p.statement)

    # En Caso <identifier>
    @_('EN_CASO NAME Cuando')
    def statement(self, p):
        # todo: EN CASO NODE
        # EN_CASO Node
        # Token: ("EnCaso_statement", p.NAME, p.Cuando)
        # Children: [p.NAME, p.Cuando]
        return ('EnCaso_statement', p.NAME, p.Cuando)

    # Cuando < relational operator> < ID | INTEGER > En tons <statements>
    # todo: revisar el caso en que no es un numero y si un NAME
    @_('CUANDO LT NUMBER EnTons',
       'CUANDO LE NUMBER EnTons',
       'CUANDO GT NUMBER EnTons',
       'CUANDO GE NUMBER EnTons',
       'CUANDO EQUAL NUMBER EnTons',
       'CUANDO NOT_EQUAL NUMBER EnTons')
    def Cuando(self, p):
        # todo: Cuando node
        # Cuando_statement Node
        # Token: ('CUANDO_statement', p[1], p.NUMBER, p.EnTons)
        # Children: [p[1], p.NUMBER,p.EnTons]
        return ('CUANDO_statement', p[1], p.NUMBER, p.EnTons)

    # En tons <statemetns> Sino <statements> Fin En caso |En tons <statemetns> Cuando <statements>
    @_('EN_TONS LBRACE statement RBRACE Cuando')
    def EnTons(self, p):
        # todo: EnTons Node
        # EnTons Node
        # Token: ('EnTons-Cuando_statement', p.statement, p.Cuando)
        # Children: [p.statement, p.Cuando]
        return ('EnTons-Cuando_statement', p.statement, p.Cuando)

    # En tons <statemetns> Sino <statements> Fin En caso |En tons <statemetns> Cuando <statements>
    @_('EN_TONS LBRACE statement RBRACE Sino')
    def EnTons(self, p):
        # EnTons Node
        # Token: ('EnTons-Fin_statement', p.statement, p.Sino)
        # Children: [p.statement, p.Sino]

        return ('EnTons-Fin_statement', p.statement, p.Sino)

    # Si No
    @_('SI_NO LBRACE statement RBRACE FIN_EN_CASO')
    def Sino(self, p):
        # todo: Sino Node
        # SiNo Node
        # Token: (SiNo_statement, p.statement)
        # Children: [p.statement]

        print("Not implemented, SINO")
        return ('SiNo_statement', p.statement)

    # def statement
    @_('DEF NAME LPAREN RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        # todo: Def NODE
        # DEF Node
        # Token: (DEF_statement, p.NAME, p.statemen)
        # Children: (p.NAME, p.statement)

        # todo: where should I add the symbol table for the scope???
        return ('DEF_statement', p.NAME, p.statement)

    # ********************************* INCLUDED FUNCTIONS *********************************#
    # TODO: AGREGAR PRODUCCIONES PARA PARAMETROS DE DEF
    # TODO: AGREGAR PARAMETRO PRINCIPAL
    # TODO: test

    # Abanico A - B
    @_('ABANICO LPAREN LETTER_B RPAREN SEMI',
       'ABANICO LPAREN LETTER_A RPAREN SEMI')
    def statement(self, p):
        # Abanico Node
        # Token: (ABANICO_statement, p[2])
        # Children: [p[2]]
        return ('ABANICO_statement', p[2])

    # Vertical I - D
    @_('VERTICAL LPAREN LETTER_I RPAREN SEMI',
       'VERTICAL LPAREN LETTER_D RPAREN SEMI')
    def statement(self, p):
        # Vertical Node
        # Token: (VERTICAL_statement, p[2])
        # Children: [p[2]]
        return ('VERTICAL_statement', p[2])

    # PERCUTOR A - B - I - D
    @_('PERCUTOR LPAREN LETTER_A RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_B RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_D RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_I RPAREN SEMI')
    def statement(self, p):
        # Percutor Node
        # Token: (PERCUTOR_statemen, p[2])
        # Children: [p[2]]
        return ('PERCUTOR_statemen', p[2])

    # PERCUTOR AMBOS LADOS
    @_(
        'PERCUTOR LPAREN LETTER_A LETTER_B RPAREN SEMI',
        'PERCUTOR LPAREN LETTER_D LETTER_I RPAREN SEMI', )
    def statement(self, p):
        # Percutor Node
        # Token: (PERCUTOR_statemen, p[2] + p[3])
        # Children: [p[2]]
        return ('PERCUTOR_statemen', p[2] + p[3])

    # GOLPE
    @_('GOLPE LPAREN RPAREN SEMI')
    def statement(self, p):
        # Golpe Node
        # Token: (GOLPE_statement, 1)
        # Children: [1]
        return ('GOLPE_statement', 1)

    # VIBRATO
    @_('VIBRATO LPAREN NUMBER RPAREN SEMI')
    def statement(self, p):
        # Vibrato Node
        # Token: (VIBRATO_statement, p.NUMBER)
        # Children: [p.NUMBER]
        return ('VIBRATO_STATEMENT', p.NUMBER)

    # METRONOMO
    @_('METRONOMO LPAREN LETTER_A RPAREN SEMI',
       'METRONOMO LPAREN LETTER_D RPAREN SEMI')
    def statement(self, p):
        # Metronomo Node
        # Token: (METRONOMO_statement,p[2])
        # Children: [p[2]]
        return ('METRONOMO_statement', p[2])

    # PRINT
    @_('PRINT LPAREN STRING RPAREN SEMI',
       'PRINT LPAREN NAME RPAREN SEMI',
       'PRINT LPAREN expr RPAREN SEMI',
       'PRINT LPAREN NUMBER RPAREN SEMI')
    def statement(self, p):
        # Print Node
        # Token: (PRINT_statement)
        # Children: [p[2])
        return ('PRINT_statement', p[2])

    # todo: simplificar el .F y .T en uno solo

    # FALSE - TRUE OPERATORS
    @_('NAME PERIOD LETTER_T SEMI')
    def statement(self, p):
        # BoolOp Node
        # Token: (BOOLOP_statement, p.NAME, 1)
        # Children: [p.NAME, 1]
        return ('BOOLOP_statement', p.NAME, 1)

    @_('NAME PERIOD LETTER_F SEMI')
    def statement(self, p):
        # BoolOp Node
        # Token: (BOOLOP_statement, p.NAME, 0)
        # Children: [p.NAME, 0]
        return ('BOOLOP_statement', p.NAME, 0)

    # NEGATION
    @_('NAME PERIOD NEGATION SEMI')
    def statement(self, p):
        # Negation Node
        # Token: (BOOL_NEG_statement,p.NAME)
        # Children: [p.NAME]
        return ('BOOL_NEG_statement', p.NAME)

    # *********************************  Expression Operator Expression  ********************************* #
    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr MODULE expr',
       'expr INT_DIVIDE expr')
    def expr(self, p):
        # Expression Node
        # Token: ('binary-expression', p[1], p.expr0, p.expr1)
        # Operator: p[1]
        # Children: [p.expr0, p.expr1]
        return ('binary-expression', p[1], p.expr0, p.expr1)

    @_('expr LT expr',
       'expr LE expr',
       'expr GT expr',
       'expr GE expr',
       'expr EQUAL expr',
       'expr NOT_EQUAL expr', )
    def expr(self, p):
        # Expression Node
        # Token: ('condition-expression', p[1], p.expr0, p.expr1)
        # Operator: p[1]
        # Children: [p.expr0, p.expr1]
        return ('condition-expression', p[1], p.expr0, p.expr1)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        # Expression Node
        # Token: ('grouped', p.expr)
        # Children: [p.expr]
        return ('grouped', p.expr)

    @_('NUMBER')
    def expr(self, p):
        # Number Node
        # Token: ('int', p.NUMBER)
        # Children: []
        # Value: p.NUMBER
        return ('int', int(p.NUMBER))

    @_('NAME')
    def expr(self, p):
        try:
            # Name Node
            # Token: ('identifier', p.NAME)
            # Children: []
            # Value: p.NAME
            return self.names[p.NAME]
        except LookupError:
            print(f'Undefined name {p.NAME!r}')
            return 0


if __name__ == '__main__':
    lexer = Lexer.CalcLexer()
    parser = CalcParser()
    text = 'EN_CASO @var CUANDO < 2  EN_TONS { DEF @metodo(){@var1 = 666} } CUANDO < 5  EN_TONS { @var2 = 2 } SI_NO{ @var3 = 5 } FIN_EN_CASO '
    print(parser.parse(lexer.tokenize(text)))
    ## Symbol table,,,, print !!!!!!!!
    print("Symbol Table: ")
    for name in parser.names:
        print("Name: ", name, "Value: ", parser.names[name])
