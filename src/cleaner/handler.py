#returns message if not defined when called
def id_not_defined(id):
    return "ID, '" + str(id) + "', is not defined"

#returns message id created when called
def id_saved(id):
    return "'" + str(id) + "' declared succesfully"

#returns original string without the quotes
def string_cleaner(line):
    if(isinstance(line, str)):
        return line[1:-1]
    return None
