import ply.lex as lex
from File import fileRead


#Reserved Words

actions = {
'createData': 'CREATEDATA',
'setRoutes': 'SETROUTES',
'readData': 'READDATA',
'httpGet': 'HTTPGET',
'start': 'START',
'createServer': 'CREATESERVER',


}

reserved = {
'port': 'PORT',
'json': 'JSON',
'url': 'URL',
'body': 'BODY',
'object': 'OBJECT',
'Help' : 'HELP'
}

reserved.update(actions)


tokens = [
    'INT',
    'ID',
    'STRING',
    'LP',
    'RP',
    'LC',
    'RC',
    'COMMA',
    'SEMICOLON',
    'COLON',
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

#COMMENTS
def t_STRING(t):
    r'\"(.*?)"'
    return t

#COMMENTS
def t_COMMENTS(t):
    r'\// . * \\'
    pass

#Equal Sign Token
t_EQUAL = r'='

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


#Ignored Characters
t_ignore = '\t \n'


#Error
def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

#Build Lexer
lexer = lex.lex()

lexer.input(fileRead())

#
# while True:
#     tok = lexer.token()
#     if not tok : break
#     print(tok)

#print(tokenList)