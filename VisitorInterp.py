#!/usr/bin/env python3
"""Visitor simples que avalia expressões geradas pela gramática Expr.
Requer que o parser seja gerado com a opção `-visitor`.
"""
import sys
from generated.ExprVisitor import ExprVisitor
from generated.ExprParser import ExprParser


class VisitorInterp(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.env = {}

    # start_ : statement (SEMI statement)* EOF ;
    def visitStart_(self, ctx:ExprParser.Start_Context):
        results = []
        for i in range(len(ctx.statement())):
            results.append(self.visit(ctx.statement(i)))
        return results

    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.env[name] = value
        return value

    def visitAdditive(self, ctx:ExprParser.AdditiveContext):
        # children: multiplicative (op multiplicative)*
        n = ctx.getChildCount()
        res = self.visit(ctx.getChild(0))
        i = 1
        while i < n:
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i+1))
            if op == '+':
                res = res + rhs
            else:
                res = res - rhs
            i += 2
        return res

    def visitMultiplicative(self, ctx:ExprParser.MultiplicativeContext):
        n = ctx.getChildCount()
        res = self.visit(ctx.getChild(0))
        i = 1
        while i < n:
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i+1))
            if op == '*':
                res = res * rhs
            else:
                res = res / rhs
            i += 2
        return res

    def visitExponential(self, ctx:ExprParser.ExponentialContext):
        # unary (POW exponential)?
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unary())
        base = self.visit(ctx.unary())
        exp = self.visit(ctx.exponential())
        return base ** exp

    def visitUnary(self, ctx:ExprParser.UnaryContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.unary())
        return +val if op == '+' else -val

    def visitPrimary(self, ctx:ExprParser.PrimaryContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.env:
                raise NameError(f"Variavel '{name}' nao definida")
            return self.env[name]
        # '(' expr ')'
        return self.visit(ctx.expr())


if __name__ == '__main__':
    from antlr4 import FileStream, CommonTokenStream
    if len(sys.argv) < 2:
        print("Uso: python VisitorInterp.py <arquivo> (ou pipedir)")
        sys.exit(1)
    stream = FileStream(sys.argv[1])
    from generated.ExprLexer import ExprLexer
    from generated.ExprParser import ExprParser
    lexer = ExprLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.start_()
    v = VisitorInterp()
    print(v.visit(tree))
