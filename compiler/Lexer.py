from sly import Lexer
import Tokens

class CalcLexer(Lexer):
    tokens = Tokens.tokens

    # Tokens
    NAME = Tokens.t_ID
    NUMBER = Tokens.t_INTEGER

    # Operators
    # todo: Agregar operador exponencial

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

    # Dos puntos
    COLON = Tokens.t_COLON

    # Ignored pattern
    ignore_newline = r'\n+'
    ignore = ' \t'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
