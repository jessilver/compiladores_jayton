# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#start_.
    def enterStart_(self, ctx:ExprParser.Start_Context):
        pass

    # Exit a parse tree produced by ExprParser#start_.
    def exitStart_(self, ctx:ExprParser.Start_Context):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#additive.
    def enterAdditive(self, ctx:ExprParser.AdditiveContext):
        pass

    # Exit a parse tree produced by ExprParser#additive.
    def exitAdditive(self, ctx:ExprParser.AdditiveContext):
        pass


    # Enter a parse tree produced by ExprParser#multiplicative.
    def enterMultiplicative(self, ctx:ExprParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by ExprParser#multiplicative.
    def exitMultiplicative(self, ctx:ExprParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by ExprParser#exponential.
    def enterExponential(self, ctx:ExprParser.ExponentialContext):
        pass

    # Exit a parse tree produced by ExprParser#exponential.
    def exitExponential(self, ctx:ExprParser.ExponentialContext):
        pass


    # Enter a parse tree produced by ExprParser#unary.
    def enterUnary(self, ctx:ExprParser.UnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#unary.
    def exitUnary(self, ctx:ExprParser.UnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#primary.
    def enterPrimary(self, ctx:ExprParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ExprParser#primary.
    def exitPrimary(self, ctx:ExprParser.PrimaryContext):
        pass



del ExprParser