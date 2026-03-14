from antlr4 import InputStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# texto de teste — ajuste conforme sua gramática
data = "1+2*3"

lexer = ExprLexer(InputStream(data))
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)

print("Regras:", parser.ruleNames)

# usar a primeira regra como entrada (bom para testes rápidos)
start_rule = parser.ruleNames[0]
print("Usando regra de entrada:", start_rule)

parse_func = getattr(parser, start_rule)
tree = parse_func()
print(tree.toStringTree(recog=parser))
