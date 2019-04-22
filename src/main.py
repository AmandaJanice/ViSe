from functionality import Server

#Will be used as main
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    s = Server()

    #This code is running the coding sample
    s.create_server("server", 5000)
    s.update_variables("data", '{}')
    s.update_variables("data2", '{"name": "Juana", "lastName": "Petraca"}')
    s.add_route("server", '/app/send', "send")
    s.create_data("send", "data")
    # s.create_data("send", "data2")
    s.add_route("server", '/app/get', "get")
    s.read_data("get", "data")
    s.update_variables("home_text", '{"Hello":"world"}')
    s.add_route("server", '/', "home")
    s.read_data("home", "home_text")
    # s.add_endpoints("server", '/', lambda : 'Hello, World')#placeholder, necessary for execution

    ## testing for communicating with other server
    # test = httpGet(url= “https://reqres.in/api/users?page=2”);
    # test_route = server: setRoutes(url= "/test");
    # test_route: readData(body= test);
    s.update_variables("test", s.http_get("https://reqres.in/api/users?page=2"))
    s.add_route("server", '/test', "test_route")
    s.read_data("test_route", "test")

    #testing non Id route call: server: setRoutes(url= "/empty"): readData(body: Data2)
    s.read_data(s.add_route("server", "/empty"), "data2")
    s.start_server("server")
