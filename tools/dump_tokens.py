#!/usr/bin/env python3
import sys, argparse
from antlr4 import FileStream, InputStream, Token

try:
    from generated.ExprLexer import ExprLexer
except Exception:
    try:
        from ExprLexer import ExprLexer
    except Exception:
        print("ExprLexer não encontrado. Gere o parser (veja README).")
        sys.exit(1)

def main():
    ap = argparse.ArgumentParser(description="Imprime tokens (lexer).")
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
    symbolic = getattr(ExprLexer, "symbolicNames", None)
    literal = getattr(ExprLexer, "literalNames", None)

    i = 0
    t = lexer.nextToken()
    while t.type != Token.EOF:
        name = None
        if symbolic and t.type < len(symbolic):
            name = symbolic[t.type]
        elif literal and t.type < len(literal):
            name = literal[t.type]
        else:
            name = str(t.type)
        print(f"{i}\t{name}\t{t.text}")
        i += 1
        t = lexer.nextToken()

if __name__ == "__main__":
    main()
