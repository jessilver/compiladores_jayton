grammar Expr;

// Parser (regras):
start_ : statement+ EOF ;

statement      : declaration SEMI
               | assignment SEMI
               | expr SEMI 
               ;

// Adicionada a regra de declaração
declaration : TYPE ID (ATTRIB expr)? ;
assignment     : ID ATTRIB expr ;

// A cadeia de precedência DEVE ser estrita (uma chama a próxima)
expr           : additive ;
additive       : multiplicative ( (PLUS | MINUS) multiplicative )* ;
multiplicative : exponential ( (STAR | SLASH) exponential )* ;
exponential    : unary ( POW exponential )? ; 
unary          : (PLUS | MINUS) unary | primary ;
primary        : FLOAT | INT | ID | LPAREN expr RPAREN ;


// Símbolos e operadores
ATTRIB : '='  ;  // atribuição
SEMI   : ';'  ;  // separador
POW    : '**' ;  // potência
PLUS   : '+'  ;  // soma
MINUS  : '-'  ;  // subtração
STAR   : '*'  ;  // multiplicação
SLASH  : '/'  ;  // divisão
LPAREN : '('  ;  // abre parênteses
RPAREN : ')'  ;  // fecha parênteses

// Palavras-chave e Tipos (DEVE vir antes do ID)
TYPE : 'int' | 'float' ;

// Literais e identificadores corrigidos
FLOAT : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
INT   : [0-9]+ ;                    
ID    : [a-zA-Z_] [a-zA-Z_0-9]* ;   
WS    : [ \t\r\n]+ -> skip ;