grammar Expr;

// Parser (regras):
start_ : expr (SEMI expr)* EOF ;

expr : additive ;
additive : multiplicative ( (PLUS | MINUS) multiplicative )* ;
multiplicative : exponential ( (STAR | SLASH) exponential )* ;
exponential : unary ( POW exponential )? ; // '**' é right-assoc
unary : (PLUS | MINUS) unary | primary ;
primary : INT | ID | LPAREN expr RPAREN ;

// Lexer (tokens):
SEMI : ';' ;
POW : '**' ;
PLUS : '+' ;
MINUS : '-' ;
STAR : '*' ;
SLASH : '/' ;
LPAREN : '(' ;
RPAREN : ')' ;

INT : [0-9]+ ;
ID : [a-zA-Z_] [a-zA-Z_0-9]* ;
WS : [ \t\r\n]+ -> skip ;

// Para regenerar: antlr4 -Dlanguage=Python3 -o generated Expr.g4