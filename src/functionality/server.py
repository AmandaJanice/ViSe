from flask import Flask
from flask import request
import json
import requests as req
import logging

class Route_ID():
    def __init__(self, route, server_id):
        self.route = route
        self.server_id = server_id

class Server_ID():
    def __init__(self, flask_instance, port):
        self.flask_instance = flask_instance
        self.port = port

class Server():

    def __init__(self, variables={}):
        self.variables = variables #parser stores id's to this dict
        self.used_ports = []

    def update_variables(self, var_id, object):
        parsed = json.loads(object)

        try:
            #check if values in variables and replaces them with appropriate variables
            for key in parsed:
                if parsed[key] in self.variables:
                    parsed[key] = self.variables[parsed[key]]

            self.variables[var_id] = parsed

        except:
            self.variables[var_id] = parsed

    def add_route(self, server_id, route, route_id = None):
        if(not route_id):
            route_id = server_id + route
        self.variables[route_id] = Route_ID(route, server_id)

        return route_id

    def add_endpoints(self, server_id, route_endpoint, action):
        app = self.variables[server_id].flask_instance

        # app.add_url_rule('/', 'Home', lambda : 'Hello, World')

        app.add_url_rule(route_endpoint, str(route_endpoint), action)

        return

    def create_data(self, route_id, object_id):#TODO PUT and POST
        endpoint = self.variables[route_id]

        def create_action():
            self.variables[object_id] = request.get_json()
            return str(self.variables[object_id])

        self.add_endpoints(endpoint.server_id, endpoint.route, create_action)

    def read_data(self, route_id, object_id):#TODO GET
        endpoint = self.variables[route_id]

        def return_action():
            return str(self.variables[object_id])

        self.add_endpoints(endpoint.server_id, endpoint.route, return_action)

    def create_server(self, assigned_id, port=80):
        if(port not in self.used_ports):
            self.variables[assigned_id] = Server_ID(Flask(assigned_id), port)
            self.used_ports.append(port)
            return "Server instance created at port: " + str(port) + "\n (Server not running) Run " + assigned_id + ": start; to run server"
        else:
            raise Exception("Not accepted, port: " + str(port) + ", is already in use")

    def start_server(self, server_id):
        try:
            self.variables[server_id].flask_instance.run(port=self.variables[server_id].port)
            return "Server started at: http://localhost/" + str(self.variables[server_id].port) + "/"
        except:
            raise Exception("server failed to start")

    ## TODO: add httpGet function
    def http_get(self, url):
        return json.dumps(req.get(url).json())
