# Visual Server
A Programming lenguage for the creation of servers

### Coding Example
```
//if port parameter is empty by default is 80\\
server = createServer (port: 3000);

//Create variable for data storage\\
data = json: {};
data2 = json: {“name”: “Juana”, “lastName”: “Petraca”};

//Server receives\\
send = server: setRoutes(url: “/app/send”);

//uses the request body in a JSON format\\
send: createData(object: data);  //object: object to save into\\
send: createData(object: data2);//you can overwrite existing values\\

//Server sends\\
get = server: setRoutes(url: “/app/get”);
get: readData(body: data); //data in JSON format\\

server: start;

```
