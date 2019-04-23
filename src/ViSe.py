import ViSeParser as parser

def run():
    parse = parser.parser
    while True:
       try:
           s = input('ViSe >> ')
       except EOFError:
           break
       if not s: continue
       elif s == "Exit" or "exit":
           break
       result = parse.parse(s)
       print(result)

run()