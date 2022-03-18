# Reserved words
t_ignore = ' \t'

tokens = {  # Literals (identifier)
    'NAME', 'NUMBER',

    # Operators (+, -, *, **, //, / , <, <=,  >, >=, ==, <>)
    'PLUS', 'MINUS', 'TIMES','INT_DIVIDE', 'DIVIDE', 'MODULE',

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
