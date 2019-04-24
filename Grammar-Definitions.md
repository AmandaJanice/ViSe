**Visual Server (ViSe) Definition**

**Tokens**

Character   ::=  a-z | A-Z | ? | \_ | ~ | &quot;+&quot; | - | &quot;\*&quot; | &amp; | > | < | (Everything that isn&#39;t in other tokens)

Digit       ::=  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |9

Delimiter   ::=  (  |  )  |  [ |  ] | &quot;{&quot; | &quot;}&quot; | , | ; | &quot; | / | \

Operator    ::=  = | :

**Grammar**

Exp ::= Def | SecondaryExp | Id : Start | Id ; | HttpGet ;

Def ::= Id = Prim ; | Id = Object ; | Id = SecondaryExp ; | Id = Int ;

SecondaryExp ::= Id : Second | Id : Third

Object ::= json : &quot;{&quot;&quot;}&quot; | json : &quot;{&quot;{ String : ObjectParam , }\* String : ObjectParam &quot;}&quot; | HttpGet

ObjectParam ::= String | Id | Exp

Prim  ::= CreateServer

Second ::= SetRoutes | SetRoutes : Third

Third ::= CreateData | ReadData

Start ::= start ;

HttpGet ::= httpGet (from = String)

ReadData ::= readData (body = Id)

SetRoutes ::= setRoutes (url = String)

CreateData ::= createData (object = Id)

CreateServer ::= createServer () | createServer (port = Int)

String ::= &quot; {Character | Digit | Delimiter | Operator}\* &quot;

Comment ::= // {Character | Digit | Delimiter | Operator}\* \\\\

Id ::= Character {Character | Int}\*

Int ::= Digit+
