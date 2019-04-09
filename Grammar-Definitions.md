**Visual Server (ViSe) Definition**

**Tokens**

Character   ::=  a-z | A-Z | ? | \_ | ~ | &quot;+&quot; | - | &quot;\*&quot; | &amp; | > | < | (Everything that isn&#39;t in other tokens)

Digit       ::=  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |9

Delimiter   ::=  (  |  )  |  [ |  ] | &quot;{&quot; | &quot;}&quot; | , | ; | &quot; | / | \

Operator    ::=  = | :

**Grammar**

Exp         ::= Def+ | Prim | Prim : Second | Id : Second | Object

Object ::= json: &quot;{&quot;&quot;}&quot; | json: &quot;{&quot;{ ObjectParam : ObjectParam , } ObjectParam : ObjectParam &quot;}&quot;

ObjectParam ::= String | Id | Exp

Def ::= Id = Exp ;

Prim  ::= HttpGet | CreateServer

Second ::= SetRoutes | CreateData | ReadData | start

HttpGet ::= httpGet (from = TextRef)

ReadData ::= readData (body = Ref)

SetRoutes ::= setRoutes (url = TextRef)

CreateData ::= createData (object = Ref)

CreateServer ::= createServer () | createServer (port = Int)

TextRef ::= Id | String

Ref ::= Id | Object

String ::= &quot; {Character | Digit | Delimiter | Operator}\* &quot;

Comment ::= // {Character | Digit | Delimiter | Operator}\* \\

Id ::= Character {Character | Int}\*

Int ::= Digit+
