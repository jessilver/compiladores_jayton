import os
import sys

from antlr4 import InputStream, CommonTokenStream

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATED_DIR = os.path.join(BASE_DIR, "generated")

if GENERATED_DIR not in sys.path:
	sys.path.insert(0, GENERATED_DIR)

from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser

# texto de teste — ajuste conforme sua gramática
data = "a=3+4*5"

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
