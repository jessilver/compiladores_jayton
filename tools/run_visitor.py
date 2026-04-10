#!/usr/bin/env python3
import sys
from antlr4 import FileStream, CommonTokenStream

try:
    from generated.ExprLexer import ExprLexer
    from generated.ExprParser import ExprParser
except Exception:
    print('Erro: módulos gerados não encontrados. Gere o parser primeiro.')
    sys.exit(1)

from VisitorInterp import VisitorInterp

if len(sys.argv) < 2:
    print('Uso: run_visitor.py <arquivo>')
    sys.exit(1)

stream = FileStream(sys.argv[1])
lexer = ExprLexer(stream)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
tree = parser.start_()
v = VisitorInterp()
print(v.visit(tree))
