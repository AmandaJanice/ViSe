# Visual Server
A Programming lenguage for the creation of servers

### Coding Example
```
//if port parameter is empty by default is 80\\
server = createServer (port= 3000);

//Create variable for data storage\\
data = json: {};
data2 = json: {"name": "8%%$", "lastName": "Petraca", "age": "67"};

//Server receives\\
send = server: setRoutes(url= "/app/send");

//uses the request body in a JSON format\\
send: createData(object= data);  //object: object to save into\\
//send: createData(object= data2);//you can also overwrite existing values but b\\\\

//Server sends\\
get = server: setRoutes(url= "/app/get");
get: readData(body= data); //data in JSON format\\

server: setRoutes(url= "/empty"): readData(body= data2);
server: setRoutes(url= "/empty"): createData(object= data2);

server: start;

//Communicating with other server\\
test = httpGet(url= "https://reqres.in/api/users?page=2");
//receives JSON from another server\\

```

### Using the source
To use this, first you need to install the required dependencies.
On a virtual environment (preferrably) run: ```pip install -r requirements.txt```

Then you can run the interpreter with ```python src/ViSe.py```
(This requires Python 3.7 or higher)
