# Visual Server

<iframe width="560" height="315" src="https://www.youtube.com/embed/p5X6shu7544" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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

### Language Features
- Simple local server creation and communication with external servers
- Declarative, dynamically typed and functional programming language
- Single line route assignment	
- Does not mix with a database
  - Simplicity is key. We don't transfer data for its storage, only for simple send/receive operations
- Easy to use for IOT projects
  - You can easily set it up on a small computer to receive commands and send responses

