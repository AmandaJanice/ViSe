from functionality import Server

#Will be used as main
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    s = Server()

    #This code is running the coding sample
    s.create_server("server", 5000)
    s.update_variables("data", '{}')
    s.update_variables("data2", '{"name": "Juana", "lastName": "Petraca"}')
    s.add_route("send", "server", "/app/send")
    s.add_endpoints("server", '/', lambda : 'Hello, World')#placeholder, necessary for execution
    s.start_server("server")
