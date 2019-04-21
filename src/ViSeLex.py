import ply.lex as lex
from File import fileRead


#Reserved Words

actions = {
'createData': 'CREATEDATA',
'setRoutes': 'SETROUTES',
'readData': 'READDATA',
'httpGET': 'HTTPGET',
'start': 'START',
'createServer': 'CREATESERVER',


}

reserved = {
'port': 'PORT',
'json': 'JSON',
'from': 'FROM',
'url': 'URL',
'body': 'BODY',
'object': 'OBJECT',
}

reserved.update(actions)


tokens = [
    'INT',
    'UNKNOWN',
    'ID',
    'STRING',
    'LP',
    'RP',
    'LC',
    'RC',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'PERIOD',
    'PLUS',
    'CHARACTER',
    'COMMENTS',
    'BSLASH',
    'SLASH',
    'DQUOTE',
    'EQUAL'

] + list(reserved.values())

# Regular expressions rules for simple tokens

#Rule for Numbers (INT)
def t_INT(t):
    r'(\d+)'
    return t

# Rule for Variables and Reserved Words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


#Unknown Character Token
t_UNKNOWN = r'\?'

#COMMENTS
def t_STRING(t):
    r'\" . * "'
    return t

#COMMENTS
def t_COMMENTS(t):
    r'\// . * \\'
    pass

#Back Slash Token
t_BSLASH = r'\\'

#Slash Token
t_SLASH = r'\/'

#Equal Sign Token
t_EQUAL = r'='

#DQUOTE Token
t_DQUOTE = r'\"'

#Left Parenthesis Token
t_LP = r'\('

#Right Parenthesis Token
t_RP = r'\)'

#Left Curly Token
t_LC = r'\{'

#Right Curly Token
t_RC = r'\}'

#Comma Curly Token
t_COMMA = r','

#Semicolon Token
t_SEMICOLON = r';'

#Colon Token
t_COLON = r':'

#Period Symbol Token
t_PERIOD = r'\.'

#Rule for Characters
def t_CHARACTER(t):
    r'\[~+-<>$%&.!]'
    return t

#Ignored Characters
t_ignore = '\t \n'


#Error
def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

#Build Lexer
lexer = lex.lex()

lexer.input(fileRead())
# tokenList = []
#
# while True:
#     tok = lexer.token()
#     if not tok : break
#     tokenList.append(tok)
#     print(tok)

#print(tokenList)