
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOL DIVIDE ELSE EQ GE GT ID IF INT LE LPAREN LT MINUS NEQ OR PLUS RPAREN SCOPE SEMICOLON TIMES WHILEprogram : statementsstatements : statement statements\n                  | emptystatement : assignment\n                 | if_statement\n                 | while_statementassignment : ID ASSIGN expression SEMICOLONif_statement : IF LPAREN expression RPAREN SCOPE statements SCOPE else_blockelse_block : ELSE SCOPE statements SCOPE\n                  | emptywhile_statement : WHILE LPAREN expression RPAREN SCOPE statements SCOPEexpression : expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | factorfactor : INT\n              | BOOL\n              | ID\n              | LPAREN expression RPARENempty :'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,11,24,41,42,43,45,48,],[-22,0,-1,-22,-3,-4,-5,-6,-2,-7,-22,-11,-8,-10,-9,]),'ID':([0,3,5,6,7,12,13,14,21,24,25,26,27,28,37,38,41,42,43,45,46,48,],[8,8,-4,-5,-6,15,15,15,15,-7,15,15,15,15,8,8,-22,-11,-8,-10,8,-9,]),'IF':([0,3,5,6,7,24,37,38,41,42,43,45,46,48,],[9,9,-4,-5,-6,-7,9,9,-22,-11,-8,-10,9,-9,]),'WHILE':([0,3,5,6,7,24,37,38,41,42,43,45,46,48,],[10,10,-4,-5,-6,-7,10,10,-22,-11,-8,-10,10,-9,]),'SCOPE':([3,4,5,6,7,11,24,30,31,37,38,39,40,41,42,43,44,45,46,47,48,],[-22,-3,-4,-5,-6,-2,-7,37,38,-22,-22,41,42,-22,-11,-8,46,-10,-22,48,-9,]),'ASSIGN':([8,],[12,]),'LPAREN':([9,10,12,13,14,21,25,26,27,28,],[13,14,21,21,21,21,21,21,21,21,]),'INT':([12,13,14,21,25,26,27,28,],[19,19,19,19,19,19,19,19,]),'BOOL':([12,13,14,21,25,26,27,28,],[20,20,20,20,20,20,20,20,]),'TIMES':([15,17,18,19,20,32,33,34,35,36,],[-20,27,-17,-18,-19,27,27,-15,-16,-21,]),'DIVIDE':([15,17,18,19,20,32,33,34,35,36,],[-20,28,-17,-18,-19,28,28,-15,-16,-21,]),'SEMICOLON':([15,16,17,18,19,20,32,33,34,35,36,],[-20,24,-14,-17,-18,-19,-12,-13,-15,-16,-21,]),'PLUS':([15,16,17,18,19,20,22,23,29,32,33,34,35,36,],[-20,25,-14,-17,-18,-19,25,25,25,-12,-13,-15,-16,-21,]),'MINUS':([15,16,17,18,19,20,22,23,29,32,33,34,35,36,],[-20,26,-14,-17,-18,-19,26,26,26,-12,-13,-15,-16,-21,]),'RPAREN':([15,17,18,19,20,22,23,29,32,33,34,35,36,],[-20,-14,-17,-18,-19,30,31,36,-12,-13,-15,-16,-21,]),'ELSE':([41,],[44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,3,37,38,46,],[2,11,39,40,47,]),'statement':([0,3,37,38,46,],[3,3,3,3,3,]),'empty':([0,3,37,38,41,46,],[4,4,4,4,45,4,]),'assignment':([0,3,37,38,46,],[5,5,5,5,5,]),'if_statement':([0,3,37,38,46,],[6,6,6,6,6,]),'while_statement':([0,3,37,38,46,],[7,7,7,7,7,]),'expression':([12,13,14,21,],[16,22,23,29,]),'term':([12,13,14,21,25,26,],[17,17,17,17,32,33,]),'factor':([12,13,14,21,25,26,27,28,],[18,18,18,18,18,18,34,35,]),'else_block':([41,],[43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parser.py',6),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',10),
  ('statements -> empty','statements',1,'p_statements','parser.py',11),
  ('statement -> assignment','statement',1,'p_statement','parser.py',18),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',19),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',20),
  ('assignment -> ID ASSIGN expression SEMICOLON','assignment',4,'p_assignment','parser.py',24),
  ('if_statement -> IF LPAREN expression RPAREN SCOPE statements SCOPE else_block','if_statement',8,'p_if_statement','parser.py',28),
  ('else_block -> ELSE SCOPE statements SCOPE','else_block',4,'p_else_block','parser.py',32),
  ('else_block -> empty','else_block',1,'p_else_block','parser.py',33),
  ('while_statement -> WHILE LPAREN expression RPAREN SCOPE statements SCOPE','while_statement',7,'p_while_statement','parser.py',40),
  ('expression -> expression PLUS term','expression',3,'p_expression','parser.py',44),
  ('expression -> expression MINUS term','expression',3,'p_expression','parser.py',45),
  ('expression -> term','expression',1,'p_expression','parser.py',46),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',53),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',54),
  ('term -> factor','term',1,'p_term','parser.py',55),
  ('factor -> INT','factor',1,'p_factor','parser.py',62),
  ('factor -> BOOL','factor',1,'p_factor','parser.py',63),
  ('factor -> ID','factor',1,'p_factor','parser.py',64),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',65),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',73),
]
