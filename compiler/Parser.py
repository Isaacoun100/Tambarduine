#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

import Lexer
from sly import Parser
from AST.Node import *
from AST.AbstractSyntaxTree import *

"""
Class for the parser
"""


class CalcParser(Parser):
    tokens = Lexer.CalcLexer.tokens

    def __init__(self):
        self.names = {}

    @_('NAME ASSIGN expr')
    def statement(self, p):
        token = "assignment"
        children = [p.NAME, p.expr]
        # Create the node and fill its children and GYM
        node = Assignment()
        node.setToken(token)
        node.setChildren(children)

        self.names[p.NAME] = p.expr
        return node

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
        setNode = Set()
        # Token: ("SET_statement, p.Name, p.expr)
        token = "Set-statement"
        setNode.setToken(token)
        # Children: [p.Name, p.expr]
        children = [p.NAME, p.expr]
        return setNode

    # IF statement
    @_('IF LPAREN expr RPAREN LBRACE statement RBRACE Else')
    def statement(self, p):
        # IF NODE
        node = If()
        # Token: ('IF_statement', p.expr, p.statement, p.Else)
        token = "If-statement"
        # Children: [p.expr, p.statement, p.Else]
        children = [p.expr, p.statement, p.Else]
        return Node

    # ELSE statement
    @_('ELSE  LBRACE statement RBRACE')
    def Else(self, p):
        # ELSE Node
        node = Else()

        # Token: ("ELSE_statement, p.statement)
        token = "Else"
        # Children: [p.statement]
        children = [p.statement]
        return node

    # FOR statement
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN STEP LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        # FOR Node
        node = For()
        # Token: ("FOR_statement,p[2], p[6], p[10], p.statement
        token = "FOR-statement"

        # Children: [p[2], p[6], p[10], p.statement]
        n3 = p[10]
        n1 = p[2]
        n2 = p[6]
        children = [n1, n2, n3, p.statement]
        return node

    # FOR statement NO STEP
    @_('FOR LPAREN NUMBER RPAREN TO LPAREN NUMBER RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        # FOR Node
        node = For()
        # Token: ("FOR_statement,p[2], p[6], p[10], p.statement
        token = "FOR-statement"

        # Children: [p[2], p[6], p[10], p.statement]
        n3 = 1
        n1 = p[2]
        n2 = p[6]
        children = [n1, n2, n3, p.statement]

        node.setChildren(children)
        node.setToken(token)

        return node

    # En Caso <identifier>
    @_('EN_CASO NAME Cuando')
    def statement(self, p):
        # EN_CASO Node
        node = En_Caso()
        # Token: ("EnCaso_statement", p.NAME, p.Cuando)
        token = "EnCaso"
        # Children: [p.NAME, p.Cuando]
        token = [p.NAME, p.Cuando]
        children = [p.NAME, p.Cuando]
        node.setChildren(children)
        node.setToken(token)

        return node

    # Cuando < relational operator> < ID | INTEGER > En tons <statements>
    @_('CUANDO LT NUMBER EnTons',
       'CUANDO LE NUMBER EnTons',
       'CUANDO GT NUMBER EnTons',
       'CUANDO GE NUMBER EnTons',
       'CUANDO EQUAL NUMBER EnTons',
       'CUANDO NOT_EQUAL NUMBER EnTons')
    def Cuando(self, p):
        # Cuando_statement Node
        node = Cuando_statement()
        # Token: ('CUANDO_statement', p[1], p.NUMBER, p.EnTons)
        token = "Cuando"
        node.setToken(token)
        # Children: [p[1], p.NUMBER,p.EnTons]
        children = [p[1], p.NUMBER, p.EnTons]
        node.setChildren(children)
        return node

    # En tons <statemetns> Sino <statements> Fin En caso |En tons <statemetns> Cuando <statements>
    @_('EN_TONS LBRACE statement RBRACE Cuando')
    def EnTons(self, p):
        # EnTons Node
        node = EnTons_statement()
        # Token: ('EnTons-Cuando_statement', p.statement, p.Cuando)
        token = "EnTons"
        node.setToken(token)
        # Children: [p.statement, p.Cuando]
        children = [p.statement, p.Cuando]
        node.setChildren(children)
        return node

    # En tons <statemetns> Sino <statements> Fin En caso |En tons <statemetns> Cuando <statements>
    @_('EN_TONS LBRACE statement RBRACE Sino')
    def EnTons(self, p):
        # EnTons Node
        node = EnTons_statement()

        # Token: ('EnTons-Fin_statement', p.statement, p.Sino)
        token = "EnTons"
        node.setToken(token)
        # Children: [p.statement, p.Sino]
        children = [p.statement, p.Sino]
        node.setChildren(children)

        return node

    # Si No
    @_('SI_NO LBRACE statement RBRACE FIN_EN_CASO')
    def Sino(self, p):
        # SiNo Node
        node = Sino_statement()

        # Token: (SiNo_statement, p.statement)
        token = "Sino"
        node.setToken(token)

        # Children: [p.statement]
        children = [p.statement]
        node.setChildren(children)

        return node

    # def statement
    @_('DEF NAME LPAREN RPAREN LBRACE statement RBRACE')
    def statement(self, p):
        # DEF Node
        node = Def()

        # Token: (DEF_statement, p.NAME, p.statement)
        token = "Def"
        node.setToken(token)
        # Children: (p.NAME, p.statement)
        children = [p.NAME, p.statement]
        node.setChildren(children)

        # todo: where should I add the symbol table for the scope???
        return node

    # ********************************* INCLUDED FUNCTIONS *********************************#
    # TODO: AGREGAR PRODUCCIONES PARA PARAMETROS DE DEF
    # TODO: AGREGAR PARAMETRO PRINCIPAL
    # TODO: test

    # Abanico A - B
    @_('ABANICO LPAREN LETTER_B RPAREN SEMI',
       'ABANICO LPAREN LETTER_A RPAREN SEMI')
    def statement(self, p):
        # Abanico Node
        node = Abanico()
        # Token: (ABANICO_statement, p[2])
        token = "Abanico"
        node.setToken(token)
        # Children: [p[2]]
        children = [p[2]]
        node.setChildren(children)
        return node

    # Vertical I - D
    @_('VERTICAL LPAREN LETTER_I RPAREN SEMI',
       'VERTICAL LPAREN LETTER_D RPAREN SEMI')
    def statement(self, p):
        # Vertical Node
        node = Vertical()
        # Token: (VERTICAL_statement, p[2])
        token = "Vertical"
        node.setToken(token)
        # Children: [p[2]]
        children = [p[2]]
        node.setChildren(children)
        return node

    # PERCUTOR A - B - I - D
    @_('PERCUTOR LPAREN LETTER_A RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_B RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_D RPAREN SEMI',
       'PERCUTOR LPAREN LETTER_I RPAREN SEMI')
    def statement(self, p):
        # Percutor Node
        node = Percutor()
        # Token: (PERCUTOR_statemen, p[2])
        token = "Percutor"
        node.setToken(token)
        # Children: [p[2]]
        children = [p[2]]
        node.setChildren(children)
        return node

    # PERCUTOR AMBOS LADOS
    @_(
        'PERCUTOR LPAREN LETTER_A LETTER_B RPAREN SEMI',
        'PERCUTOR LPAREN LETTER_D LETTER_I RPAREN SEMI', )
    def statement(self, p):
        # Percutor Node
        node = Percutor()
        # Token: (PERCUTOR_statemen, p[2] + p[3])
        token = "Percutor"
        node.setToken(token)
        # Children: [p[2]]
        input = str(p[2]) + str(p[3])
        children = [input]
        node.setChildren(children)
        return node

    # GOLPE
    @_('GOLPE LPAREN RPAREN SEMI')
    def statement(self, p):
        # Golpe Node
        node = Golpe()

        # Token: (GOLPE_statement, 1)
        token = "Golpe"
        node.setToken(token)
        # Children: [1]
        children = [1]
        node.setChildren(children)
        return node

    # VIBRATO
    @_('VIBRATO LPAREN NUMBER RPAREN SEMI')
    def statement(self, p):
        # Vibrato Node]
        node = Vibrato()
        # Token: (VIBRATO_statement, p.NUMBER)
        token = "Vibrato"
        node.setToken(token)
        # Children: [p.NUMBER]
        children = [p.NUMBER]
        node.setChildren(children)
        return node

    # METRONOMO
    @_('METRONOMO LPAREN LETTER_A RPAREN SEMI',
       'METRONOMO LPAREN LETTER_D RPAREN SEMI')
    def statement(self, p):
        # Metronomo Node
        node = Metronomo()
        # Token: (METRONOMO_statement,p[2])
        token = "Metronomo"
        node.setToken(token)
        # Children: [p[2]] -> A | D
        children = [p[2]]
        node.setChildren(children)
        return ('METRONOMO_statement', p[2])

    # PRINT
    @_('PRINT LPAREN STRING RPAREN SEMI',
       'PRINT LPAREN NAME RPAREN SEMI',
       'PRINT LPAREN expr RPAREN SEMI',
       'PRINT LPAREN NUMBER RPAREN SEMI')
    def statement(self, p):
        # Print Node
        node = Print()

        # Token: (PRINT_statement)
        token = "Print"
        node.setToken(token)
        # Children: [p[2])
        children = [p[2]]
        node.setChildren(children)
        return node

    # todo: simplificar el .F y .T en uno solo

    # FALSE - TRUE OPERATORS
    @_('NAME PERIOD LETTER_T SEMI')
    def statement(self, p):
        # BoolOp Node
        node = BoolOp()
        # Token: (BOOLOP_statement, p.NAME, 1)
        token = "Bool Op"
        node.setToken(token)
        # Children: [p.NAME, 1]
        children = [p.NAME, 1]
        node.setChildren(children)
        return node

    @_('NAME PERIOD LETTER_F SEMI')
    def statement(self, p):
        # BoolOp Node
        node = BoolOp()

        # Token: (BOOLOP_statement, p.NAME, 0)
        token = "Bool Op"
        node.setToken(token)

        # Children: [p.NAME, 1]
        children = [p.NAME, 0]
        node.setChildren(children)
        return node

    # NEGATION
    @_('NAME PERIOD NEGATION SEMI')
    def statement(self, p):
        # Negation Node
        node = Negation()

        # Token: (BOOL_NEG_statement,p.NAME)
        token = "Bool Neg"
        node.setToken(token)
        # Children: [p.NAME]
        children = [p.NAME]
        node.setChildren(children)
        return node

    # *********************************  Expression Operator Expression  ********************************* #
    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr MODULE expr',
       'expr INT_DIVIDE expr')
    def expr(self, p):
        # Expression Node
        operator = p[1]
        node = Expression(operator)
        # Token: ('binary-expression', p[1], p.expr0, p.expr1)
        token = "Binary-Expression"
        node.setToken(token)
        # Operator: p[1]
        node.setOperator(operator)
        # Children: [p.expr0, p.expr1]
        children = [p.expr0, p.expr1]
        node.setChildren(children)

        return node

    @_('expr LT expr',
       'expr LE expr',
       'expr GT expr',
       'expr GE expr',
       'expr EQUAL expr',
       'expr NOT_EQUAL expr', )
    def expr(self, p):
        # Expression Node
        operator = p[1]
        node = Expression(operator)
        # Token: ('condition-expression', p[1], p.expr0, p.expr1)
        token = "condition-Expression"
        node.setToken(token)
        # Operator: p[1]
        node.setOperator(operator)
        # Children: [p.expr0, p.expr1]
        children = [p.expr0, p.expr1]
        node.setChildren(children)

        return node

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        # Expression Node
        node = Expression()
        # Token: ('grouped', p.expr)
        token = "Grouped"
        node.setToken(token)
        # Children: [p.expr]
        children = [p.expr]
        node.setChildren(children)
        return node

    @_('NUMBER')
    def expr(self, p):
        # Number Node
        # Token: ('int', p.NUMBER)
        # Children: []
        # Value: p.NUMBER
        return int(p.NUMBER)

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


