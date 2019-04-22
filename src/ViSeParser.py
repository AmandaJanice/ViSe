import ply.yacc as parse
from ViSeLex import tokens


precedence = (
    ('right','EQUAL'),
    ('left','LP'),
    ('left','LC'),
    ('right','RP'),
    ('right','RC')
)

def p_Exp_Def(p):
    'Exp : Def'
    print("ExpDef")

def p_Exp_Prim_Empty(p):
    'Exp : Id COLON Prim'
    print("ExpPrimEmpty")


def p_Exp_Prim_Second(p):
    'Exp : Prim COLON Second'
    print("ExpPrimSecond")


def p_Exp_Id_Second(p):
    'Exp : Id COLON Second'
    print("ExpIdSecond")


def p_Exp_Object(p):
    'Exp : Object SEMICOLON'
    print("ExpObject")


def p_Object_Empty(p):
    'Object : JSON COLON LC RC'
    print("JSON COLON LC RC")


def p_Inside_Object(p):
    'Inside : ID COLON ObjectParam'

def p_Inside_ObjectRec(p):
    'InsideRec : ID COLON ObjectParam COMMA Inside'

def p_Object(p):
    'Object : JSON COLON LC Inside RC'
    print("JSON COLON LC Inside RC")

def p_ObjectHttpGet(p):
    'Object : HttpGet'

def p_Object_VARIOUS(p):
    'Object : JSON COLON LC InsideRec RC'
    print("JSON COLON LC Inside Rec RC")

def p_ObjectParam_String(p):
    'ObjectParam : String'
    print("ObjectParam_String")

def p_ObjectParam_Id(p):
    'ObjectParam : Id'
    print("ObjectParam_Id")

def p_ObjectParam_Exp(p):
    'ObjectParam : Exp'
    print("ObjectParam_Exp")

def p_Def_Id_Exp(p):
    'Def : ID EQUAL Exp SEMICOLON'
    print("ID EQUAL Exp SEMICOLON")


def p_Prim_CreateServer(p):
    'Prim : CreateServer'
    print("Prim : CreateServer")


def p_second_set_routes(p):
    'Second : SetRoutes'
    print("Second : SetRoutes")


def p_second_create_data(p):
    'Second : CreateData'
    print("Second : CreateData")


def p_second_read_data(p):
    'Second : ReadData'
    print("Second : ReadData")


def p_Second_start(p):
    'Second : START'
    print("Second : start")


def p_http_get(p):
    'HttpGet : HTTPGET LP FROM EQUAL TextRef RP'
    print("HttpGet")


def p_http_get_url(p):
    'HttpGet : HTTPGET LP URL EQUAL STRING RP'
    print("HttpGet URL")


def p_read_data(p):
    'ReadData : READDATA LP BODY EQUAL Ref RP'
    print("ReadData")


def p_set_routes(p):
    'SetRoutes : SETROUTES LP URL EQUAL STRING RP'
    print("SetRoutes")


def p_create_data(p):
    'CreateData : CREATEDATA LP OBJECT EQUAL Ref RP'
    print("CreateData")


def p_create_server_empty(p):
    'CreateServer : CREATESERVER LP RP'
    print("CreateServer Empty")


def p_create_server_port(p):
    'CreateServer : CREATESERVER LP PORT EQUAL Int RP'
    print("CreateServer Port")


def p_text_ref_id(p):
    'TextRef : Id'
    print("TextRef Id")


def p_text_ref_string(p):
    'TextRef : String'
    print("TextRef String")


def p_ref_id(p):
    'Ref : Id'
    print("Ref Id")


def p_ref_object(p):
    'Ref : Object'
    print("Ref Object")


#terminales
def p_string_empty(p):
    'String : DQUOTE DQUOTE'
    print("String Empty")


#terminales
def p_String(p):
    'String : STRING'
    print("String")


#terminales
def p_Id(p):
    'Id : ID'
    print("ID")


#terminales
def p_Int(p):
    'Int : INT'
    print("Int")

def p_error(p):
    print("Syntax error at ’%s’" % p)

#Build Parser
parser = parse.yacc()

while True:
   try:
       s = input('ViSe >> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)