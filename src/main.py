from functionality import Server

#Will be used as main
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    s = Server()

    #This code is running the coding sample
    s.create_server("server", 5000)
    s.update_variables("data", '{}')
    s.update_variables("data2", '{"name": "Juana", "lastName": "Petraca"}')
    s.add_route("send", "server", '/app/send')
    s.create_data("send", "data")
    # s.create_data("send", "data2")
    s.add_route("get", "server", '/app/get')
    s.read_data("get", "data")
    s.update_variables("home_text", '{"Hello":"world"}')
    s.add_route("home", "server", '/')
    s.read_data("home", "home_text")
    # s.add_endpoints("server", '/', lambda : 'Hello, World')#placeholder, necessary for execution
    s.update_variables("test", s.http_get("https://reqres.in/api/users?page=2"))
    s.add_route("test_route", "server", '/test')
    s.read_data("test_route", "test")
    s.start_server("server")
