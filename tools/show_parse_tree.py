#!/usr/bin/env python3
import sys, argparse
from pathlib import Path
from antlr4 import FileStream, InputStream, CommonTokenStream

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser

def main():
    ap = argparse.ArgumentParser(description="Imprime a parse tree (toStringTree).")
    ap.add_argument("-s", "--string", help="Texto de entrada")
    ap.add_argument("-f", "--file", help="Arquivo de entrada")
    args = ap.parse_args()
    if args.file:
        stream = FileStream(args.file)
    elif args.string:
        stream = InputStream(args.string)
    else:
        ap.print_help()
        sys.exit(1)

    lexer = ExprLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.start_()

    print('Regras:', parser.ruleNames)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
