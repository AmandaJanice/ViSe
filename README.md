## Visual Server

### Tutorial
<iframe width="560" height="315" src="https://www.youtube.com/embed/p5X6shu7544" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> \n </iframe>


### Introduction
What is IoT? The internet of things, or IoT, is a system of interrelated computing devices, mechanical and digital machines, objects, animals or people that are provided with unique identifiers (UIDs) and the ability to transfer data over a network without requiring human-to-human or human-to-computer interaction. Now imagine yourself on the verge of creating your first device. The simplest way is to create a small server. How complicated can this be? It depends really. Nothing is tough, it totally depends on your source and the way you are learning things. 

What do we bring the table? Introducing Visual Server (ViSe), a programming language for servers. With this language you can easily and simply start a server, setup the routes and begin sending or receiving requests. Our motivation behind this language is to lower the entry barrier into the IoT industry by making simplicity our greatest weapon. 	

From the creation of severs to the assignation of routes, it is all done in less than 10 lines of code. How do we do this ? We only worry about send and receive operations to your server. These two operations are essentially the key for anyone to begin working on any IoT device. That is the beauty of ViSe. Our goal is that one day, developers look at our language as their first choice for starting IoT products and say that ViSe is the future of “do it yourself” IoT devices.

### Motivation
Simple local server creation and communication with external servers

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

### Language Features
- Simple local server creation and communication with external servers
- Declarative, dynamically typed and functional programming language
- Single line route assignment	
- Does not mix with a database
  - Simplicity is key. ViSe doesn't transfer data for permanent storage, only for simple send/receive operations
- Easy to use for IOT projects
  - You can easily set it up on a small computer to receive commands and send responses

### Approach
ViSe (Visual Sever) is a resulting programming language from the necessity of simplifying the creation of servers and helping curios developers that are looking for better and easier ways to solve this challenges. Must users looking to work with servers usually have other plans that there looking to work, there obviously not directly interested on working with servers. Here were we come in, ViSe offers the simple and easiest way to work with servers, so you don’t have to spend all your precious time learning the depths of servers. 

With the upcoming times, it is only logical that servers will keep evolving and changing some kind of structure of way or another. That means ViSe will also keep evolving while at the same time having the same mindset from day one, looking to simplified server creation and communication in the simplest and easiest way possible. 

### Using the source
To use this, first you need to install the required dependencies.
On a virtual environment (preferrably) run: ```pip install -r requirements.txt```

Then you can run the interpreter with ```python src/ViSe.py```
(This requires Python 3.7 or higher)


#### Contributors:
- Amanda Vazquez [@AmandaJanice](https://github.com/AmandaJanice)
- Javier Ortiz [@jaortiz117](https://github.com/jaortiz117)
- Luis Rivera [@luisrivera1](https://github.com/luisrivera1)
