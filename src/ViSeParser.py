import ply.yacc as parse
from ViSeLex import tokens
from functionality import server as s


code = s.Server()


# precedence = (
#     ('left','LP'),
#     ('left','LC'),
#     ('right','RP'),
#     ('right','RC')
# )

#data = json: {};
#data2 = json: {"name": "8%%$", "lastName": "Petraca", "age": "67"};
def p_object_def_empty(p):
    'Exp : ID EQUAL JSON COLON LC RC SEMICOLON'
    code.update_variables(p[1], "{}")
    p[0] = p[1] + " saved."


def p_object_def(p):
    'Exp : ID EQUAL JSON COLON LC Inside RC SEMICOLON'
    code.update_variables(p[1], "{"+p[6]+"}")
    p[0] = p[1]+" saved successfully"


def p_object_def_rec(p):
    'Exp : ID EQUAL JSON COLON LC InsideRec RC SEMICOLON'
    code.update_variables(p[1], "{"+p[6]+"}")
    p[0] = p[1] + " saved succesfully"


def p_inside_object(p):
    'Inside :  STRING COLON STRING '
    p[0] = str(p[1])+str(p[2])+str(p[3])


def p_inside_rec(p):
    'InsideRec : Inside COMMA Inside COMMA Inside'
    p[0] = str(p[1])+str(p[2])+str(p[3])+str(p[4])+str(p[5])


def p_variable(p):
    'Exp : ID SEMICOLON'
    if p[1] not in code.variables:
        p[0] = "Variable not declared"
    else:
        for i in code.variables:
            if p[1] == i:
                p[0] = code.print_object(i)
                pass


def p_exp_create_server(p):
    'Exp : ID EQUAL CREATESERVER LP PORT EQUAL INT RP SEMICOLON'
    code.create_server(p[1], p[7])
    p[0] = "Server with Id: '"+p[1]+"' and port: '"+p[7]+"' created."


def p_server_start(p):
    'Exp : ID COLON START SEMICOLON'
    if p[1] not in code.variables:
        p[0] = "Server Id not in use"
    else:
        code.start_server(p[1])
        p[0] = "Server with Id: " + p[1] + "is Running at: "


def p_communicate_id(p):
    'Exp : ID EQUAL HTTPGET LP URL EQUAL STRING RP SEMICOLON'
    p[0] = code.update_variables(p[1], code.http_get(p[7][1:-1]))


def p_communicate(p):
    'Exp : HTTPGET LP URL EQUAL STRING RP SEMICOLON'
    p[0] = code.http_get(p[5][1:-1])



def p_server_sets(p):
    'Exp : ID EQUAL ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLON'
    if p[3] not in code.variables:
        p[0] = p[3]+ " not defined"
    else:
        code.add_route(p[3], p[9][1:-1], p[1])
        p[0] = "Route added successfully"


def p_server_reads(p):
    'Exp : ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON'
    if p[7] not in code.variables:
        p[0] = p[7] + "not defined"
    elif p[1] not in code.variables:
        p[0] = p[1] + "not defined"
    else:
        code.read_data(p[1], p[7])
        p[0] = "Action added"

def p_server_creates(p):
    'Exp : ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON'
    # p[0] = "p1" + p[1] + "p7" + p[7]
    if(p[7] not in code.variables):
        p[0] = p[7] + " not defined"
    elif p[1] not in code.variables:
        p[0] = p[1] + " not defined"
    else:
        code.create_data(p[1], p[7])
        p[0] = "Action added"
        # p[0] = "send: " + p[1] + " data " + p[7]


# def p_exp_def(p):
#     'Exp : Def '
#     p[0] = p[1]
#
#
# def p_exp_prim_scolon(p):
#     'Exp : Prim SEMICOLON'
#     p[0] = (p[1],p[2])
#
#
# def p_exp_prim(p):
#     'Exp : Prim'
#     p[0] = p[1]
#
#
# def p_exp_second_empty_scolon(p):
#     'Exp : Id COLON Second SEMICOLON'
#     print("ExpSecond")
#
#
# def p_exp_second(p):
#     'Exp : Second'
#     p[0]=p[1]
#
#
# def p_exp_prim_empty(p):
#     'Exp : Id COLON Prim SEMICOLON'
#     p[0] = (p[1],p[2],p[3],p[4])
#
#
# def p_exp_object(p):
#     'Exp : Object SEMICOLON'
#     p[0] = (p[1],p[2])
#
#
# def p_object_empty(p):
#     'Object : JSON COLON LC RC'
#     p[0] = (p[3],p[4])
#
#
# def p_inside_object(p):
#     'Inside : STRING COLON ObjectParam'
#     p[0] = (p[1], p[2], p[3])
#
#
# def p_inside_object_rec(p):
#     'InsideRec : ID COLON ObjectParam COMMA Inside'
#     #p[0] = (p[])
#
#
# def p_object(p):
#     'Object : JSON COLON LC Inside RC'
#     #print("JSON COLON LC Inside RC")
#     p[0] = (p[1], p[2], p[3], p[4], p[5])
#
#
# def p_ObjectHttpGet(p):
#     'Object : HttpGet'
#
#
# def p_Object_VARIOUS(p):
#     'Object : JSON COLON LC InsideRec RC'
#     print("JSON COLON LC Inside Rec RC")
#
# def p_ObjectParam_String(p):
#     'ObjectParam : String'
#     print("ObjectParam_String")
#
# def p_ObjectParam_Id(p):
#     'ObjectParam : Id'
#     print("ObjectParam_Id")
#
# def p_ObjectParam_Exp(p):
#     'ObjectParam : Exp'
#     print("ObjectParam_Exp")
#
#
# def p_def_id_exp(p):
#     'Def : ID EQUAL Exp'
#     print("ID EQUAL Exp")
#
#
# def p_def_id_exp_scolon(p):
#     'Def : ID EQUAL Exp SEMICOLON'
#     print("ID EQUAL Exp SEMICOLON")
#
#
# def p_Prim_CreateServer(p):
#     'Prim : CreateServer'
#     print("Prim : CreateServer")
#
#
# def p_second_set_routes(p):
#     'Second : SetRoutes'
#     print("Second : SetRoutes")
#
#
# def p_second_create_data(p):
#     'Second : CreateData'
#     print("Second : CreateData")
#
#
# def p_second_read_data(p):
#     'Second : ReadData'
#     print("Second : ReadData")
#
#
# def p_Second_start(p):
#     'Second : START'
#     print("Second : start")
#
#
# def p_http_get(p):
#     'HttpGet : HTTPGET LP FROM EQUAL TextRef RP'
#     print("HttpGet")
#
#
# def p_http_get_url(p):
#     'HttpGet : HTTPGET LP URL EQUAL STRING RP'
#     print("HttpGet URL")
#
#
# def p_read_data(p):
#     'ReadData : READDATA LP BODY EQUAL Ref RP'
#     print("ReadData")
#
#
# def p_set_routes(p):
#     'SetRoutes : SETROUTES LP URL EQUAL STRING RP'
#     print("SetRoutes")
#
#
# def p_create_data(p):
#     'CreateData : CREATEDATA LP OBJECT EQUAL Ref RP'
#     print("CreateData")
#
#
# def p_create_server_empty(p):
#     'CreateServer : CREATESERVER LP RP'
#     print("CreateServer Empty")
#
#
# def p_create_server_port(p):
#     'CreateServer : CREATESERVER LP PORT EQUAL Int RP'
#     print("CreateServer Port")
#
#
# def p_text_ref_id(p):
#     'TextRef : Id'
#     print("TextRef Id")
#
#
# def p_text_ref_string(p):
#     'TextRef : String'
#     print("TextRef String")
#
#
# def p_ref_id(p):
#     'Ref : Id'
#     print("Ref Id")
#
#
# def p_ref_object(p):
#     'Ref : Object'
#     print("Ref Object")
#
#
# #terminales
# def p_string_empty(p):
#     'String : DQUOTE DQUOTE'
#     print("String Empty")
#
#
# #terminales
# def p_String(p):
#     'String : STRING'
#     print("String")
#
#
# #terminales
# def p_Id(p):
#     'Id : ID'
#     p[0] = p[1]
#
# #terminales
# def p_Int(p):
#     'Int : INT'
#     print("Int")

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
