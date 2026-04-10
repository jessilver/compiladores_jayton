#!/usr/bin/env python3
import sys, argparse
from antlr4 import FileStream, InputStream, CommonTokenStream, ParseTreeWalker, ParseTreeListener

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

class TraceListener(ParseTreeListener):
    def __init__(self, parser):
        self.parser = parser

    def enterEveryRule(self, ctx):
        name = self.parser.ruleNames[ctx.getRuleIndex()]
        print(f"enter {name}: {ctx.getText()}")

    def exitEveryRule(self, ctx):
        name = self.parser.ruleNames[ctx.getRuleIndex()]
        print(f"exit  {name}: {ctx.getText()}")

def main():
    ap = argparse.ArgumentParser(description="Mostra enter/exit de regras durante walk.")
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

    walker = ParseTreeWalker()
    listener = TraceListener(parser)
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
