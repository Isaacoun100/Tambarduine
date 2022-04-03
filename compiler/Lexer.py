#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from sly import Lexer
import Tokens


class CalcLexer(Lexer):
    tokens = Tokens.tokens

    # Tokens
    NAME = Tokens.t_ID
    NUMBER = Tokens.t_INTEGER
    STRING = Tokens.t_STRING

    # Especial Tokens
    IF = Tokens.t_IF
    ELSE = Tokens.t_ELSE

    FOR = Tokens.t_FOR
    TO = Tokens.t_TO
    STEP = Tokens.t_STEP

    SET = Tokens.t_SET

    EN_CASO = Tokens.t_EN_CASO
    CUANDO = Tokens.t_CUANDO
    EN_TONS = Tokens.t_EN_TONS
    SI_NO = Tokens.t_SI_NO
    FIN_EN_CASO = Tokens.t_FIN_EN_CASO

    # Operators
    PLUS = Tokens.t_PLUS
    MINUS = Tokens.t_MINUS
    TIMES = Tokens.t_TIMES
    DIVIDE = Tokens.t_DIVIDE
    INT_DIVIDE = Tokens.t_INT_DIVIDE
    MODULE = Tokens.t_MODULE

    # Lower than - Lower Equal
    LT = Tokens.t_LT
    LE = Tokens.t_LE

    # Greater than - Greater Equal
    GE = Tokens.t_GE
    GT = Tokens.t_GT

    # Equal - Not equal
    EQUAL = Tokens.t_EQ
    NOT_EQUAL = Tokens.t_NE

    # Assignment
    ASSIGN = Tokens.t_ASSIGN

    # Delimiters
    LPAREN = Tokens.t_LPAREN
    RPAREN = Tokens.t_RPAREN

    # Punto
    PERIOD = Tokens.t_PERIOD
    # { - }
    LBRACE = Tokens.t_LBRACE
    RBRACE = Tokens.t_RBRACE

    # Punto y Coma
    SEMI = Tokens.t_SEMI
    COMMA = Tokens.t_COMMA

    # Dos puntos
    COLON = Tokens.t_COLON

    # FUNCTIONS
    DEF = Tokens.t_DEF
    ABANICO = Tokens.t_ABANICO
    VERTICAL = Tokens.t_VERTICAL
    PERCUTOR = Tokens.t_PERCUTOR
    GOLPE = Tokens.t_GOLPE
    VIBRATO = Tokens.t_VIBRATO
    METRONOMO = Tokens.t_METRONOMO
    PRINT = Tokens.t_PRINT

    # LETRAS PARA LAS FUNCIONES

    LETTER_A = Tokens.t_LETTER_A
    LETTER_B = Tokens.t_LETTER_B
    LETTER_D = Tokens.t_LETTER_D
    LETTER_I = Tokens.t_LETTER_I

    LETTER_T = Tokens.t_LETTER_T
    LETTER_F = Tokens.t_LETTER_F

    NEGATION = Tokens.t_NEGATION

    # Ignored pattern
    ignore_newline = r'\n+'
    ignore = ' \t'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
