import ply.yacc as parse
from ViSeLex import tokens
from functionality import server as s
import cleaner as cl


code = s.Server()

def p_help(p):
    'Exp : HELP'
    p[0] = "To create a server run: 'createServer (port= 3000);' and store it on a variable\nTo run the server run: 'variable : start;' \n"

def p_object_def_empty(p):
    'Exp : ID EQUAL JSON COLON LC RC SEMICOLON'
    code.update_variables(p[1], "{}")
    p[0] = cl.id_saved(p[1])


def p_object_def(p):
    'Exp : ID EQUAL JSON COLON LC Inside RC SEMICOLON'
    code.update_variables(p[1], "{"+p[6]+"}")
    p[0] = cl.id_saved(p[1])


def p_object_def_rec(p):
    'Exp : ID EQUAL JSON COLON LC InsideRec RC SEMICOLON'
    code.update_variables(p[1], "{"+p[6]+"}")
    p[0] = cl.id_saved(p[1])


def p_inside_object(p):
    'Inside :  STRING COLON STRING '
    p[0] = str(p[1])+str(p[2])+str(p[3])


def p_inside_rec(p):
    'InsideRec : Inside COMMA Inside COMMA Inside'
    p[0] = str(p[1])+str(p[2])+str(p[3])+str(p[4])+str(p[5])


def p_variable(p):
    'Exp : ID SEMICOLON'
    if p[1] not in code.variables:
        p[0] = cl.id_not_defined(p[1])
    else:
        for i in code.variables:
            if p[1] == i:
                p[0] = code.print_object(i)
                break


def p_create_server(p):
    'Exp : ID EQUAL CREATESERVER LP PORT EQUAL INT RP SEMICOLON'
    p[0] = code.create_server(p[1], p[7])


def p_create_server_empty_port(p):
    'Exp : ID EQUAL CREATESERVER LP RP SEMICOLON'
    p[0] = code.create_server(p[1])


def p_server_start(p):
    'Exp : ID COLON START SEMICOLON'
    if p[1] not in code.variables:
        p[0] = cl.id_not_defined(p[1])
    else:
        p[0] = code.start_server(p[1])


def p_communicate_id(p):
    'Exp : ID EQUAL HTTPGET LP URL EQUAL STRING RP SEMICOLON'
    code.update_variables(p[1], code.http_get(cl.string_cleaner(p[7])))
    p[0] = cl.id_saved(p[1])


def p_communicate(p):
    'Exp : HTTPGET LP URL EQUAL STRING RP SEMICOLON'
    p[0] = code.http_get(cl.string_cleaner(p[5]))


def p_server_sets(p):
    'Exp : ID EQUAL ID COLON SETROUTES LP URL EQUAL STRING RP SEMICOLON'
    if p[3] not in code.variables:
        p[0] = cl.id_not_defined(p[3])
    else:
        code.add_route(p[3], cl.string_cleaner(p[9]), p[1])
        p[0] = cl.id_saved(p[1]) + "\nRoute added successfully"


def p_server_reads(p):
    'Exp : ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON'
    if p[7] not in code.variables:
        p[0] = cl.id_not_defined(p[7])
    elif p[1] not in code.variables:
        p[0] = cl.id_not_defined(p[1])
    else:
        p[0] = code.read_data(p[1], p[7])

def p_server_read_id(p):
    'Exp : ID EQUAL ID COLON READDATA LP BODY EQUAL ID RP SEMICOLON'
    if p[9] not in code.variables:
        p[0] = cl.id_not_defined(p[9])
    elif p[3] not in code.variables:
        p[0] = cl.id_not_defined(p[3])
    else:
        code.update_variables(p[1], code.read_data(p[3], p[9]))
        p[0] = cl.id_saved(p[1])

def p_server_creates(p):
    'Exp : ID COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON'
    if(p[7] not in code.variables):
        p[0] = cl.id_not_defined(p[7])
    elif p[1] not in code.variables:
        p[0] = cl.id_not_defined(p[1])
    else:
        p[0] = code.create_data(p[1], p[7])


def p_set_routes_read(p):
    'Exp : ID COLON SETROUTES LP URL EQUAL STRING RP COLON READDATA LP BODY EQUAL ID RP SEMICOLON'
    if (p[1] not in code.variables):
        p[0] = cl.id_not_defined(p[1])
    elif p[14] not in code.variables:
        p[0] = cl.id_not_defined(p[14])
    else:
        p[0] = code.read_data(code.add_route(p[1], cl.string_cleaner(p[7])), p[14])


def p_set_routes_create(p):
    'Exp : ID COLON SETROUTES LP URL EQUAL STRING RP COLON CREATEDATA LP OBJECT EQUAL ID RP SEMICOLON'
    if (p[1] not in code.variables):
        p[0] = cl.id_not_defined(p[1])
    elif p[14] not in code.variables:
        p[0] = cl.id_not_defined(p[14])
    else:
        p[0] = code.create_data(code.add_route(p[1], cl.string_cleaner(p[7])), p[14])

def p_set_routes_non_id(p):
    'Exp : ID COLON SETROUTES LP URL LP EQUAL STRING RP SEMICOLON'
    if (p[1] not in code.variables):
        p[0] = cl.id_not_defined(p[1])
    else:
        p[0] = code.add_route(p[1], cl.string_cleaner(p[7])

def p_error(p):
    print("Syntax error at ’%s’" % p)


#Build Parser
parser = parse.yacc()
