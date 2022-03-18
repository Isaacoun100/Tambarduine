# Reserved words
t_ignore = ' \t'

tokens = {  # Literals (identifier)
    'NAME', 'NUMBER', 'STRING', 'IF', 'ELSE', 'FOR', 'TO', 'STEP', 'SET', 'EN_CASO',
    'CUANDO', 'EN_TONS', 'SI_NO', 'FIN_EN_CASO', 'NEGATION', 'TRUE_OP', 'FALSE_OP', 'ABANICO',
    'VERTICAL', 'PERCUTOR', 'GOLPE', 'VIBRATO', 'METRONOMO', 'PRINT', 'LETTER_A', 'LETTER_B', 'LETTER_I', 'LETTER_D',

    # Operators (+, -, *, **, //, / , <, <=,  >, >=, ==, <>)
    'PLUS',
    'MINUS', 'TIMES',
    'INT_DIVIDE', 'DIVIDE', 'MODULE',

    'LT', 'LE', 'GT', 'GE', 'EQUAL', 'NOT_EQUAL',

    # Assignment (=)
    'ASSIGN',

    # Delimeters ( ) { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',
}

# Operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'

t_DIVIDE = r'/'
t_INT_DIVIDE = r'//'
t_MODULE = r'%'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'<>'

# Assignment
t_ASSIGN = r'='

# Reserved words 'NEGATION', 'TRUE_OP', 'FALSE_OP', 'ABANICO',
#     'VERTICAL', 'PERCUTOR', 'GOLPE', 'VIBRATO', 'METRONOMO', 'PRINT',
t_IF = 'IF'
t_ELSE = 'ELSE'
t_FOR = 'FOR'
t_TO = 'TO'
t_STEP = 'STEP'
t_SET = 'SET'

t_LETTER_A = 'A'
t_LETTER_B = 'B'

t_LETTER_I = 'I'
t_LETTER_D = 'D'

t_ABANICO = 'Abanico'
t_VERTICAL = 'Vertical'
t_PERCUTOR = 'Percutor'
t_GOLPE = 'Golpe'
t_VIBRATO = 'Vibrato'
t_METRONOMO = 'Metronomo'
t_PRINT = 'println!'

t_NEGATION = ".Neg"
t_TRUE_OP = '.T'
t_FALSE_OP = '.F'

t_EN_CASO = 'EN_CASO'
t_CUANDO = 'CUANDO'
t_EN_TONS = 'EN_TONS'
t_SI_NO = 'SI_NO'
t_FIN_EN_CASO = 'FIN_EN_CASO'

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'

# Identifiers
t_ID = r'@[A-Za-z_][A-Za-z0-9_]*'

# Integer literal
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''
