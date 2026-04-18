#!/usr/bin/env python3
import sys
from pathlib import Path
from antlr4 import FileStream, CommonTokenStream

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser

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
