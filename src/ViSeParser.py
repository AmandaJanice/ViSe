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
    'Exp : Prim'
    print("ExpPrimEmpty")

def p_Exp_Prim_Second(p):
    'Exp : Prim COLON Second'
    print("ExpPrimSecond")

def p_Exp_Id_Second(p):
    'Exp : Id COLON Second'
    print("ExpIdSecond")

def p_Exp_Object(p):
    'Exp : Object'
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

def p_Prim_HttpGet(p):
    'Prim : HttpGet'
    print("Prim : HttpGet")

def p_Prim_CreateServer(p):
    'Prim : CreateServer'
    print("Prim : CreateServer")

def p_Second_SetRoutes(p):
    'Second : SetRoutes'
    print("Second : SetRoutes")

def p_Second_CreateData(p):
    'Second : CreateData'
    print("Second : CreateData")

def p_Second_ReadData(p):
    'Second : ReadData'
    print("Second : ReadData")

def p_Second_start(p):
    'Second : START'
    print("Second : start")

def p_HttpGet(p):
    'HttpGet : HTTPGET LP FROM EQUAL TextRef RP'
    print("HttpGet")

def p_ReadData(p):
    'ReadData : READDATA LP BODY EQUAL Ref RP'
    print("ReadData")

def p_SetRoutes(p):
    'SetRoutes : SETROUTES LP URL EQUAL TextRef RP'
    print("SetRoutes")

def p_CreateData(p):
    'CreateData : CREATEDATA LP OBJECT EQUAL Ref RP'
    print("CreateData")

def p_CreateServer_Empty(p):
    'CreateServer : CREATESERVER LP RP'
    print("CreateServer Empty")

def p_CreateServer_Port(p):
    'CreateServer : CREATESERVER LP PORT EQUAL Int RP'
    print("CreateServer Port")

def p_TextRef_Id(p):
    'TextRef : Id'
    print("TextRef Id")

def p_TextRef_String(p):
    'TextRef : String'
    print("TextRef String")

def p_Ref_Id(p):
    'Ref : Id'
    print("Ref Id")

def p_Ref_Object(p):
    'Ref : Object'
    print("Ref Object")

def p_String_Empty(p):
    'String : DQUOTE DQUOTE'
    print("String Empty")

def p_String_Id(p):
    'String : DQUOTE ID DQUOTE'
    print("String Id")

def p_String_Int(p):
    'String : DQUOTE INT DQUOTE'
    print("String Int")

def p_StringRec(p):
    'String : String'
    print("StringRec")

def p_Id(p):
    'Id : ID'
    print("ID")

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