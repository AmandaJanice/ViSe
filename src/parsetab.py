
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQUALleftLPleftLCrightRPrightRCBODY BSLASH CHARACTER COLON COMMA COMMENTS CREATEDATA CREATESERVER DQUOTE EQUAL FROM HTTPGET ID INT JSON LC LP OBJECT PERIOD PLUS PORT RC READDATA RP SEMICOLON SETROUTES SLASH START STRING UNKNOWN URLExp : DefExp : Id COLON Prim SEMICOLONExp : Prim COLON Second SEMICOLONExp : Id COLON Second SEMICOLONExp : Object SEMICOLONExp : HttpGet SEMICOLONObject : JSON COLON LC RCInside : ID COLON ObjectParamInsideRec : ID COLON ObjectParam COMMA InsideObject : JSON COLON LC Inside RCObject : JSON COLON LC InsideRec RCObjectParam : StringObjectParam : IdObjectParam : ExpObject : HttpGet SEMICOLONDef : ID EQUAL Exp SEMICOLONPrim : HttpGetPrim : CreateServerSecond : SetRoutesSecond : CreateDataSecond : ReadDataSecond : STARTHttpGet : HTTPGET LP FROM EQUAL TextRef RPHttpGet : HTTPGET LP URL EQUAL STRING RPReadData : READDATA LP BODY EQUAL Ref RPSetRoutes : SETROUTES LP URL EQUAL TextRef RPCreateData : CREATEDATA LP OBJECT EQUAL Ref RPCreateServer : CREATESERVER LP RPCreateServer : CREATESERVER LP PORT EQUAL Int RPTextRef : IdTextRef : StringRef : IdRef : ObjectString : DQUOTE DQUOTEString : STRINGId : IDInt : INT'
    
_lr_action_items = {'ID':([0,16,32,48,56,66,67,68,84,91,],[7,7,47,60,69,60,60,60,89,69,]),'JSON':([0,16,56,67,68,91,],[9,9,9,9,9,9,]),'HTTPGET':([0,12,16,56,67,68,91,],[10,10,10,10,10,10,10,]),'CREATESERVER':([0,12,16,56,91,],[11,11,11,11,11,]),'$end':([1,2,14,15,37,38,42,43,],[0,-1,-5,-6,-2,-4,-3,-16,]),'SEMICOLON':([2,5,6,8,14,15,20,21,22,23,24,25,26,30,31,35,37,38,42,43,44,54,55,74,76,77,82,85,86,88,],[-1,14,15,-18,-5,-6,37,38,-17,-19,-20,-21,-22,42,43,-28,-2,-4,-3,-16,-7,-10,-11,-23,-24,-29,87,-26,-27,-25,]),'COMMA':([2,14,15,37,38,42,43,62,69,70,71,72,73,75,],[-1,-5,-6,-2,-4,-3,-16,-35,-36,84,-12,-13,-14,-34,]),'RC':([2,14,15,32,37,38,42,43,45,46,62,69,70,71,72,73,75,90,92,],[-1,-5,-6,44,-2,-4,-3,-16,54,55,-35,-36,-8,-12,-13,-14,-34,-9,-8,]),'COLON':([3,4,6,7,8,9,35,47,69,72,74,76,77,89,],[12,13,-17,-36,-18,17,-28,56,-36,12,-23,-24,-29,91,]),'EQUAL':([7,33,34,36,51,52,53,69,],[16,48,49,50,66,67,68,16,]),'LP':([10,11,27,28,29,],[18,19,39,40,41,]),'START':([12,13,],[26,26,]),'SETROUTES':([12,13,],[27,27,]),'CREATEDATA':([12,13,],[28,28,]),'READDATA':([12,13,],[29,29,]),'LC':([17,],[32,]),'FROM':([18,],[33,]),'URL':([18,39,],[34,51,]),'RP':([19,44,54,55,57,58,59,60,62,63,64,65,75,78,79,80,81,83,87,],[35,-7,-10,-11,74,-30,-31,-36,-35,76,77,-37,-34,85,86,-32,-33,88,-15,]),'PORT':([19,],[36,]),'OBJECT':([40,],[52,]),'BODY':([41,],[53,]),'DQUOTE':([48,56,61,66,91,],[61,61,75,61,61,]),'STRING':([48,49,56,66,91,],[62,63,62,62,62,]),'INT':([50,],[65,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Exp':([0,16,56,91,],[1,31,73,73,]),'Def':([0,16,56,91,],[2,2,2,2,]),'Id':([0,16,48,56,66,67,68,91,],[3,3,58,72,58,80,80,72,]),'Prim':([0,12,16,56,91,],[4,20,4,4,4,]),'Object':([0,16,56,67,68,91,],[5,5,5,81,81,5,]),'HttpGet':([0,12,16,56,67,68,91,],[6,22,6,6,82,82,6,]),'CreateServer':([0,12,16,56,91,],[8,8,8,8,8,]),'Second':([12,13,],[21,30,]),'SetRoutes':([12,13,],[23,23,]),'CreateData':([12,13,],[24,24,]),'ReadData':([12,13,],[25,25,]),'Inside':([32,84,],[45,90,]),'InsideRec':([32,],[46,]),'TextRef':([48,66,],[57,78,]),'String':([48,56,66,91,],[59,71,59,71,]),'Int':([50,],[64,]),'ObjectParam':([56,91,],[70,92,]),'Ref':([67,68,],[79,83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Exp","S'",1,None,None,None),
  ('Exp -> Def','Exp',1,'p_Exp_Def','ViSeParser.py',14),
  ('Exp -> Id COLON Prim SEMICOLON','Exp',4,'p_Exp_Prim_Empty','ViSeParser.py',18),
  ('Exp -> Prim COLON Second SEMICOLON','Exp',4,'p_Exp_Prim_Second','ViSeParser.py',22),
  ('Exp -> Id COLON Second SEMICOLON','Exp',4,'p_Exp_Id_Second','ViSeParser.py',26),
  ('Exp -> Object SEMICOLON','Exp',2,'p_Exp_Object','ViSeParser.py',30),
  ('Exp -> HttpGet SEMICOLON','Exp',2,'p_Exp_HttpGet','ViSeParser.py',34),
  ('Object -> JSON COLON LC RC','Object',4,'p_Object_Empty','ViSeParser.py',38),
  ('Inside -> ID COLON ObjectParam','Inside',3,'p_Inside_Object','ViSeParser.py',42),
  ('InsideRec -> ID COLON ObjectParam COMMA Inside','InsideRec',5,'p_Inside_ObjectRec','ViSeParser.py',45),
  ('Object -> JSON COLON LC Inside RC','Object',5,'p_Object','ViSeParser.py',48),
  ('Object -> JSON COLON LC InsideRec RC','Object',5,'p_Object_VARIOUS','ViSeParser.py',52),
  ('ObjectParam -> String','ObjectParam',1,'p_ObjectParam_String','ViSeParser.py',56),
  ('ObjectParam -> Id','ObjectParam',1,'p_ObjectParam_Id','ViSeParser.py',60),
  ('ObjectParam -> Exp','ObjectParam',1,'p_ObjectParam_Exp','ViSeParser.py',64),
  ('Object -> HttpGet SEMICOLON','Object',2,'p_ObjectHttpGet','ViSeParser.py',67),
  ('Def -> ID EQUAL Exp SEMICOLON','Def',4,'p_Def_Id_Exp','ViSeParser.py',70),
  ('Prim -> HttpGet','Prim',1,'p_Prim_HttpGet','ViSeParser.py',74),
  ('Prim -> CreateServer','Prim',1,'p_Prim_CreateServer','ViSeParser.py',78),
  ('Second -> SetRoutes','Second',1,'p_Second_SetRoutes','ViSeParser.py',82),
  ('Second -> CreateData','Second',1,'p_Second_CreateData','ViSeParser.py',86),
  ('Second -> ReadData','Second',1,'p_Second_ReadData','ViSeParser.py',90),
  ('Second -> START','Second',1,'p_Second_start','ViSeParser.py',94),
  ('HttpGet -> HTTPGET LP FROM EQUAL TextRef RP','HttpGet',6,'p_HttpGet','ViSeParser.py',98),
  ('HttpGet -> HTTPGET LP URL EQUAL STRING RP','HttpGet',6,'p_HttpGet_Url','ViSeParser.py',102),
  ('ReadData -> READDATA LP BODY EQUAL Ref RP','ReadData',6,'p_ReadData','ViSeParser.py',106),
  ('SetRoutes -> SETROUTES LP URL EQUAL TextRef RP','SetRoutes',6,'p_SetRoutes','ViSeParser.py',110),
  ('CreateData -> CREATEDATA LP OBJECT EQUAL Ref RP','CreateData',6,'p_CreateData','ViSeParser.py',114),
  ('CreateServer -> CREATESERVER LP RP','CreateServer',3,'p_CreateServer_Empty','ViSeParser.py',118),
  ('CreateServer -> CREATESERVER LP PORT EQUAL Int RP','CreateServer',6,'p_CreateServer_Port','ViSeParser.py',122),
  ('TextRef -> Id','TextRef',1,'p_TextRef_Id','ViSeParser.py',126),
  ('TextRef -> String','TextRef',1,'p_TextRef_String','ViSeParser.py',130),
  ('Ref -> Id','Ref',1,'p_Ref_Id','ViSeParser.py',134),
  ('Ref -> Object','Ref',1,'p_Ref_Object','ViSeParser.py',138),
  ('String -> DQUOTE DQUOTE','String',2,'p_String_Empty','ViSeParser.py',142),
  ('String -> STRING','String',1,'p_String','ViSeParser.py',146),
  ('Id -> ID','Id',1,'p_Id','ViSeParser.py',150),
  ('Int -> INT','Int',1,'p_Int','ViSeParser.py',154),
]
