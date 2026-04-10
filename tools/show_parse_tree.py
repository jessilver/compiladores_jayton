#!/usr/bin/env python3
import sys, argparse
from antlr4 import FileStream, InputStream, CommonTokenStream

try:
    from generated.ExprLexer import ExprLexer
    from generated.ExprParser import ExprParser
except Exception:
    try:
        from ExprLexer import ExprLexer
        from ExprParser import ExprParser
    except Exception:
        print("ExprLexer/ExprParser não encontrados. Gere o parser primeiro.")
        sys.exit(1)

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
