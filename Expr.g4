grammar Expr;

// Parser (regras):
start_ : expr (SEMI expr)* EOF ;

expr           : additive ;
additive       : multiplicative ( (PLUS | MINUS) multiplicative )* ;
multiplicative : exponential ( (STAR | SLASH) exponential )* ;
exponential    : unary ( POW exponential )? ; // '**' é right-assoc
unary          : (PLUS | MINUS) unary | primary ;
primary        : INT | ID | LPAREN expr RPAREN ;

// Símbolos e operadores
// '**' antes de '*' para evitar conflito com STAR
SEMI   : ';'  ;  // separador
POW    : '**' ;  // potência
PLUS   : '+'  ;  // soma
MINUS  : '-'  ;  // subtração
STAR   : '*'  ;  // multiplicação
SLASH  : '/'  ;  // divisão
LPAREN : '('  ;  // abre parênteses
RPAREN : ')'  ;  // fecha parênteses

// Literais e identificadores
INT : [0-9]+ ;                      // inteiro
ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;     // identificador
WS  : [ \t\r\n]+ -> skip ;          // ignora espaços

// Para regenerar: antlr4 -Dlanguage=Python3 -o generated Expr.g4